from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch


def transform(img:Image):

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-101")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-101")
    
    inputs = processor(images = img, return_tensors = "pt")
    outputs = model(**inputs)


    target_sizes = torch.tensor([img.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    output_dict = {}
    item_number = 0

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        item_number += 1
        output_dict[f'Object {item_number}'] = {'Object Name':f'{model.config.id2label[label.item()]}'.title(), 
                                    'Match Confidence':f'{round(score.item(), 4)*100} %', 
                                    'Image Grid Coordinates':f'{box}'}
    return output_dict