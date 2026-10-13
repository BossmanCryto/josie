# JOSIE Gemini Vertex AI integration

This adds a standalone Gemini chat integration without changing the existing JOSIE runtime.

## Use

```bash
python gemini_integration.py "Explain Android Shizuku in simple terms"
python gemini_integration.py
```

## Required configuration

Add these to `~/.config/josie-connected-apps/config.env`:

```bash
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_ACCESS_TOKEN=your-short-lived-oauth-access-token
GEMINI_MODEL=gemini-2.0-flash
GOOGLE_CLOUD_LOCATION=us-central1
```

Protect the configuration:

```bash
chmod 600 ~/.config/josie-connected-apps/config.env
```

## Security rules

- Never commit `GOOGLE_ACCESS_TOKEN`, OAuth refresh tokens, API keys, or project credentials.
- Use a short-lived access token and rotate it according to Google's guidance.
- Enable only the Vertex AI scope needed for the integration.
- OAuth consent, billing activation, and API-key creation must be completed in Google's official consoles.