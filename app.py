from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import sqlite3
import pandas as pd

app = FastAPI(title="Smart Web Scraper System")

@app.get("/", response_class=HTMLResponse)
async def home():
    try:
        conn = sqlite3.connect("data/scraped_data.db")
        df = pd.read_sql("""
            SELECT title, link, source, scraped_at 
            FROM articles 
            ORDER BY scraped_at DESC LIMIT 100
        """, conn)
        conn.close()

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Smart Web Scraper Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background: #f4f4f4; }}
                table {{ width: 100%; border-collapse: collapse; background: white; }}
                th, td {{ padding: 12px; border: 1px solid #ddd; text-align: left; }}
                th {{ background: #007bff; color: white; }}
                h1 {{ color: #333; }}
                a {{ color: #0066cc; }}
            </style>
        </head>
        <body>
            <h1>Smart Web Scraper Dashboard</h1>
            <p><strong>Total Records:</strong> {len(df)}</p>
            
            <table>
                <tr>
                    <th>Title</th>
                    <th>Source</th>
                    <th>Scraped At</th>
                </tr>
        """
        
        for _, row in df.iterrows():
            html += f"""
                <tr>
                    <td><a href="{row['link']}" target="_blank">{row['title']}</a></td>
                    <td>{row['source']}</td>
                    <td>{row['scraped_at']}</td>
                </tr>
            """
        
        html += """
            </table>
        </body>
        </html>
        """
        return HTMLResponse(html)
        
    except Exception as e:
        return HTMLResponse(f"<h2>Error: {str(e)}</h2>")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
