#!/bin/bash

# IntelliExo AI Advisor Panel Quick Start Script
# One-command deployment for NVIDIA LLM RAG Demo

echo "🚀 Starting IntelliExo AI Advisor Panel - NVIDIA LLM RAG Demo"

# Check for required environment variables
if [ -z "$NVIDIA_API_KEY" ]; then
    echo "❌ Error: NVIDIA_API_KEY environment variable not set"
    echo "Please set: export NVIDIA_API_KEY=your_api_key"
    exit 1
fi

# Check for NVIDIA Docker runtime
if ! docker info | grep -q "nvidia"; then
    echo "⚠️  Warning: NVIDIA Docker runtime not detected"
    echo "For GPU acceleration, install nvidia-docker2"
fi

# Build and run the container
echo "📦 Building Docker image..."
docker build -t intelliexo-ai-advisor-panel .

echo "🏃 Running IntelliExo AI Advisor Panel..."
docker run --rm \
    --gpus all \
    -p 8501:8501 \
    -e NVIDIA_API_KEY=$NVIDIA_API_KEY \
    -e ELEVENLABS_API_KEY=$ELEVENLABS_API_KEY \
    -v $(pwd)/data:/app/data \
    -v $(pwd)/voices:/app/voices \
    --name intelliexo-ai-advisor-panel \
    intelliexo-ai-advisor-panel

echo "✅ IntelliExo AI Advisor Panel is now running at http://localhost:8501" 