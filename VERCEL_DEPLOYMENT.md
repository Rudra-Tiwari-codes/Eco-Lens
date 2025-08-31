# EcoLens Vercel Deployment Guide

## 🚀 Deploying EcoLens to Vercel

This guide will help you deploy your EcoLens sustainability app to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **OpenAI API Key**: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
3. **GitHub Repository**: Your EcoLens code should be in a GitHub repository

## Deployment Steps

### 1. Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Select the EcoLens repository

### 2. Configure Environment Variables

In your Vercel project settings, add the following environment variable:

```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

**Important**: Replace `your_actual_openai_api_key_here` with your real OpenAI API key.

### 3. Deploy Settings

- **Framework Preset**: Other
- **Build Command**: Leave empty (Vercel will auto-detect)
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### 4. Deploy

Click "Deploy" and wait for the build to complete.

## File Structure for Vercel

```
EcoLens/
├── api/
│   └── index.py          # Vercel serverless function entry point
├── public/
│   └── index.html        # Static landing page
├── src/
│   └── ecolens/
│       ├── main.py       # FastAPI application
│       └── static/
│           └── index.html # Main web interface
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
└── runtime.txt          # Python version specification
```

## Troubleshooting

### 404 Error
If you get a 404 error:
1. Check that your `vercel.json` is properly configured
2. Ensure the `api/index.py` file exists
3. Verify environment variables are set correctly

### API Key Issues
If the app doesn't work:
1. Verify your OpenAI API key is set in Vercel environment variables
2. Check that the key is valid and has sufficient credits
3. Test the API key locally first

### Build Errors
If the build fails:
1. Check that all dependencies are in `requirements.txt`
2. Verify Python version in `runtime.txt`
3. Check Vercel build logs for specific errors

## Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export OPENAI_API_KEY=your_api_key_here

# Run locally
python run.py
```

## Support

If you encounter issues:
1. Check Vercel deployment logs
2. Verify all files are committed to your repository
3. Ensure environment variables are properly set
4. Test the API endpoints manually

## Security Notes

- ✅ API keys are stored securely in Vercel environment variables
- ✅ No sensitive data is committed to the repository
- ✅ The app uses proper CORS configuration
- ✅ Static files are served correctly

---

**EcoLens** - Making environmental impact visible, one item at a time. 🌍
