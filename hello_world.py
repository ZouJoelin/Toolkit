import argparse
import torch

def main(args):
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    if torch.cuda.is_available():
        gpu_ids = list(range(torch.cuda.device_count()))
        print(f"Available GPUs: {gpu_ids}")
        device = torch.device("cuda", gpu_ids[args.gpu_id])
    else:
        device = torch.device("cpu")
        
    print(f"Using device: {device}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--gpu_id", type=int, default=0)
    args = parser.parse_args()

    main(args)


