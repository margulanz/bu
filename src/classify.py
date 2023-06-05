from torchvision import models, transforms
from PIL import Image
import torch

def classify(image_name):
	alexnet = models.alexnet(pretrained=True)
	transform = transforms.Compose([           
	    transforms.Resize(256),                   
	    transforms.CenterCrop(224),               
	    transforms.ToTensor(),                    
	    transforms.Normalize(                     
	    mean=[0.485, 0.456, 0.406],               
	    std=[0.229, 0.224, 0.225]                  
	 )])


	img = Image.open(image_name)
	img_t = transform(img)
	batch_t = torch.unsqueeze(img_t, 0)

	alexnet.eval()
	out = alexnet(batch_t)
	with open('src/labels.txt') as f:
	    classes = [line.strip() for line in f.readlines()]
	_, index = torch.max(out, 1)
	 
	percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
	return {
		'Label': classes[index[0]], 
		'percentage': percentage[index[0]].item()
		}




