import torch.utils.data as data
import torch
import dataset
import torchvision.transforms as trans

model = torch.load ("model/epoch10/e10.pt")
model.eval ()

def test () :
    transform = trans.Compose (
        [
            trans.Resize ((60, 60)),
            trans.ToTensor ()
        ]
    )
    test_set = dataset.Mydataset (
        root_dir="splited_data/test",
        transform=transform
    )

    test_loader = data.DataLoader (
        dataset=test_set,
        batch_size=10,
        shuffle=True
    )

    for step, (x, y) in enumerate (test_loader) :
        out = model (x)
        out = torch.softmax (out, 1)
        predi = torch.max (out, 1)[1]
        if step % 50 == 0 :
            print (f"{predi} \t {y}")
            
def to_onnx () :
    input_name = ['input']
    output_name = ['output']
    args = torch.randn (1, 1, 60, 60)
    # print (args)
    torch.onnx.export (
        model=model,
        args=args,
        f="model/epoch10/model_on.onnx",
        input_names=input_name,
        output_names=output_name,
        verbose=True
    )
    
to_onnx ()