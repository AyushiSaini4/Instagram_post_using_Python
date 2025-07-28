# PYTHON_TASKS_LW/instagram_poster.py

import streamlit as st
import requests

def run():
    st.title("📸 Instagram Image Poster via Graph API")

    # Input fields
    access_token = st.text_input("🔐 Facebook Graph Access Token", type="password")
    ig_user_id = st.text_input("👤 Instagram Business User ID")
    image_url = st.text_input("🌐 Image URL (publicly accessible)", "https://example.com/your-image.jpg")
    caption = st.text_area("📝 Caption", "Hello from Python! 🚀")

    if st.button("📤 Post to Instagram"):
        if not (access_token and ig_user_id and image_url and caption):
            st.warning("Please fill all fields.")
            return

        try:
            # Step 1: Create Media Object
            media_endpoint = f"https://graph.facebook.com/v18.0/{ig_user_id}/media"
            media_payload = {
                "image_url": image_url,
                "caption": caption,
                "access_token": access_token
            }
            media_response = requests.post(media_endpoint, data=media_payload)
            media_data = media_response.json()

            if 'id' not in media_data:
                st.error(f"❌ Media creation failed: {media_data}")
                return

            creation_id = media_data['id']
            st.info(f"🆔 Media Created: {creation_id}")

            # Step 2: Publish Media
            publish_endpoint = f"https://graph.facebook.com/v18.0/{ig_user_id}/media_publish"
            publish_payload = {
                "creation_id": creation_id,
                "access_token": access_token
            }
            publish_response = requests.post(publish_endpoint, data=publish_payload)
            publish_data = publish_response.json()

            if 'id' in publish_data:
                st.success(f"✅ Post published successfully! ID: {publish_data['id']}")
            else:
                st.error(f"❌ Failed to publish post: {publish_data}")

        except Exception as e:
            st.error(f"Unexpected error: {e}")
