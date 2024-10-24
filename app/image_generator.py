import replicate
import asyncio

async def generate_image(prompt: str) -> str:
    """Generates an image using the Replicate API."""
    model = "replicate/your-model-name"  # Replace with your model name

    # Run the synchronous function in a thread pool to make it compatible with async
    loop = asyncio.get_event_loop()
    output = await loop.run_in_executor(None, replicate.run, model, {"prompt": prompt})

    return output[0]  # Assuming the output is a list of URLs
