import os
import asyncio
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from server import mcp
from fastmcp import Client

load_dotenv()

async def run_gemini_mcp_chat():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("PERINGATAN: GEMINI_API_KEY belum diisi di file .env")
        api_key = input("Masukkan GEMINI_API_KEY Anda: ").strip()

    ai_client = genai.Client(api_key=api_key)

    async with Client(mcp) as mcp_client:
        # Ambil semua tool dari MCP Server
        mcp_tools = await mcp_client.list_tools()

        # Konversi MCP tool menjadi FunctionDeclaration untuk Gemini API
        function_declarations = []
        for t in mcp_tools:
            function_declarations.append(types.FunctionDeclaration(
                name=t.name,
                description=t.description or f"Tool {t.name}",
                parameters=t.inputSchema if hasattr(t, 'inputSchema') and t.inputSchema else None
            ))

        gemini_tools = [types.Tool(function_declarations=function_declarations)]

        print("\n=============================================")
        print("🤖 MCP + Gemini AI Chat Assistant")
        print("=============================================")
        print("Contoh pertanyaan yang bisa Anda tanyakan:")
        print("1. Berapa total penjualan SBN?")
        print("2. Apa produk SBN teratas berdasarkan penjualan?")
        print("3. Sapa saya dalam bahasa Indonesia.")
        print("(Ketik 'exit' untuk keluar)\n")

        chat = ai_client.chats.create(
            model="gemini-flash-lite-latest",
            config=types.GenerateContentConfig(
                tools=gemini_tools,
                temperature=0.2,
            )
        )

        while True:
            try:
                user_prompt = input("\nAnda: ").strip()
                if not user_prompt:
                    continue
                if user_prompt.lower() in ["exit", "quit", "keluar"]:
                    print("Terima kasih!")
                    break

                response = chat.send_message(user_prompt)

                # Tangani panggilan fungsi jika Gemini memilih untuk memanggil MCP tool
                while response.function_calls:
                    for call in response.function_calls:
                        print(f"\n[MCP LOG] Gemini memanggil tool '{call.name}'...")
                        
                        # Eksekusi tool melalui MCP Client
                        tool_result = await mcp_client.call_tool(call.name, dict(call.args) if call.args else {})
                        
                        raw_text = tool_result.content[0].text if tool_result.content else ""
                        try:
                            result_data = json.loads(raw_text)
                        except Exception:
                            result_data = {"result": raw_text}

                        print(f"[MCP LOG] Hasil dari tool '{call.name}': {result_data}")

                        # Kirimkan hasil eksekusi tool kembali ke Gemini
                        response = chat.send_message(
                            types.Part.from_function_response(
                                name=call.name,
                                response={"result": result_data}
                            )
                        )

                if response.text:
                    print(f"\nGemini: {response.text}")

            except KeyboardInterrupt:
                print("\nSession dihentikan.")
                break
            except Exception as e:
                print(f"\nError: {e}")

if __name__ == "__main__":
    asyncio.run(run_gemini_mcp_chat())
