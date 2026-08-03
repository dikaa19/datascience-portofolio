import asyncio
from server import mcp
from fastmcp import Client

async def main():
    print("Menghubungkan dan mengetes MCP Server (server.py)...")
    
    # Menguji MCP Server
    async with Client(mcp) as client:
        # 1. Mendapatkan daftar tool yang tersedia di server
        tools = await client.list_tools()
        print("\n--- DAFTAR TOOL TERSEDIA ---")
        for tool in tools:
            print(f"- {tool.name}")

        # 2. Menguji tool 'hello'
        print("\n--- MEMANGGIL TOOL: hello ---")
        result_hello = await client.call_tool("hello")
        print("Hasil:", result_hello.content[0].text)

        # 3. Menguji tool 'get_total_sales'
        print("\n--- MEMANGGIL TOOL: get_total_sales ---")
        result_sales = await client.call_tool("get_total_sales")
        print("Hasil Total Penjualan:", result_sales.content[0].text)

        # 4. Menguji tool 'top_product'
        print("\n--- MEMANGGIL TOOL: top_product ---")
        result_top = await client.call_tool("top_product")
        print("Hasil Produk Teratas:\n", result_top.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
