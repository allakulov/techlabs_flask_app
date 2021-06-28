from fastbook import *
from fastai.vision.widgets import *


def create_dataloader(path):
    
    print(" Creating dataloader.. ")
    db = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128))

    db = db.new(
        item_tfms=RandomResizedCrop(224, min_scale=0.5),
        batch_tfms=aug_transforms())

    dls = db.dataloaders(path)
    return dls

def train_model(dls , save_model_name = "animals_prediction.pkl"):

    print(" Training Model .. ")
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(4)
    learn.export(save_model_name)
    return learn


if __name__ == "__main__":
    path = Path("DATA")
    animals_path = (path/"animals")
    dls = create_dataloader(animals_path)
    model = train_model(dls ,"animals_prediction.pkl")

