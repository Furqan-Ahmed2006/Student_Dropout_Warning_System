import os
import time
from playwright.sync_api import sync_playwright

APP_URL = os.getenv("STREAMLIT_APP_URL", "https://your-app-name.streamlit.app")

def ping_streamlit_app():
    print(f"🚀 Launching headless browser to ping: {APP_URL}")
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
    
            page.goto(APP_URL, timeout=60000, wait_until="networkidle")
            time.sleep(5) 
            

            wake_button = page.query_selector("button:has-text('Yes, get this app back up!')")
            if wake_button:
                print("⚡ App was sleeping. Clicking Wake Up button...")
                wake_button.click()
                time.sleep(15)
            

            button = page.query_selector("button:has-text('Analyze Student Risk Status')")
            if button:
                button.click()
                print("✅ Successfully clicked prediction button!")
                time.sleep(3)
            else:
                print("ℹ️ Prediction button not found, but page pinged successfully.")
                
            print("🎉 Keep-Alive Ping Successful!")
            
        except Exception as e:
            print(f"❌ Error pinging Streamlit app: {str(e)}")
            
        finally:
            browser.close()

if __name__ == "__main__":
    ping_streamlit_app()