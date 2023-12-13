#pip install diffusers
from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")

prompt = "A beautiful lion roars."

image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]