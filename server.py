from mcp.server.fastmcp import FastMCP

# Membuat MCP Server
mcp = FastMCP("Bareksa Demo")

@mcp.tool()
def hello():
    """Sapaan sederhana."""
    return "Hello World!"

@mcp.tool()
def get_total_sales():
    """Mendapatkan total seluruh penjualan SBN."""
    import pandas as pd

    df = pd.read_csv("data/sbn_sales_per_series.csv", thousands=",")
    return int(df["total_amount"].sum())

@mcp.tool()
def top_product(top: int = 1, by: str = "total_amount", ascending: bool = False):
    """
    Mendapatkan daftar produk teratas (atau terendah) berdasarkan kriteria tertentu.
    
    Parameters:
    - top: Jumlah produk yang ingin ditampilkan (default: 1)
    - by: Kriteria pengurutan ('total_amount'/'sales', 'investors'/'investor', 'transaction_frequency', 'avg_purchase')
    - ascending: False untuk urutan tertinggi/teratas, True untuk urutan terendah.
    """
    import pandas as pd

    df = pd.read_csv("data/sbn_sales_per_series.csv", thousands=",")

    # Pemetaan alias kolom agar fleksibel
    column_mapping = {
        "sales": "total_amount",
        "total_sales": "total_amount",
        "total_amount": "total_amount",
        "investor": "investors",
        "investors": "investors",
        "frequency": "transaction_frequency",
        "transaction_frequency": "transaction_frequency",
        "avg": "avg_purchase",
        "avg_purchase": "avg_purchase"
    }

    sort_column = column_mapping.get(by.lower(), "total_amount")
    sorted_df = df.sort_values(sort_column, ascending=ascending).head(top)

    results = []
    for _, row in sorted_df.iterrows():
        results.append({
            "product": str(row["product_code"]),
            "sales": int(row["total_amount"]),
            "investors": int(str(row["investors"]).replace(",", "")),
            "transaction_frequency": int(str(row["transaction_frequency"]).replace(",", "")),
            "avg_purchase": int(str(row["avg_purchase"]).replace(",", ""))
        })

    return results

@mcp.tool()
def get_sales_data(product_code: str):
    """
    Mendapatkan detail data penjualan untuk kode produk SBN tertentu (misal: SBR003, ORI017, ST006).
    """
    import pandas as pd

    df = pd.read_csv("data/sbn_sales_per_series.csv", thousands=",")

    filtered = df[df["product_code"].astype(str).str.upper() == product_code.upper().strip()]
    if filtered.empty:
        return {"error": f"Produk dengan kode {product_code} tidak ditemukan."}

    row = filtered.iloc[0]

    return {
        "product": str(row["product_code"]),
        "sales": int(row["total_amount"]),
        "investors": int(str(row["investors"]).replace(",", "")),
        "transaction_frequency": int(str(row["transaction_frequency"]).replace(",", "")),
        "avg_purchase": int(str(row["avg_purchase"]).replace(",", ""))
    }

if __name__ == "__main__":
    mcp.run()