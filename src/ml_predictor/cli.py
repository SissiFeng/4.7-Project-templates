import argparse
import sys
from ml_predictor.model import MLPredictor, load_data

def main():
    parser = argparse.ArgumentParser(description='ML Predictor CLI')
    parser.add_argument('action', choices=['train', 'predict'], help='Action to perform')
    parser.add_argument('--data', required=True, help='Path to the data file')
    parser.add_argument('--model', required=True, help='Path to save/load the model')
    args = parser.parse_args()

    predictor = MLPredictor()

    try:
        data = load_data(args.data)
    except FileNotFoundError:
        print(f"Error: Data file '{args.data}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        sys.exit(1)

    if args.action == 'train':
        try:
            # TODO: Preprocess the data
            X, y = predictor.preprocess_data(data)
            
            # TODO: Train the model
            predictor.train(X, y)
            
            # TODO: Save the model
            predictor.save_model(args.model)
            
            print(f"Model trained and saved to {args.model}")
        except Exception as e:
            print(f"Error during training: {str(e)}")
            sys.exit(1)
    
    elif args.action == 'predict':
        try:
            # TODO: Load the model
            predictor.load_model(args.model)
            
            # TODO: Preprocess the data
            X, _ = predictor.preprocess_data(data)
            
            # TODO: Make predictions
            predictions = predictor.predict(X)
            
            print("Predictions:")
            for i, pred in enumerate(predictions):
                print(f"Sample {i+1}: {pred}")
        except FileNotFoundError:
            print(f"Error: Model file '{args.model}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            sys.exit(1)

if __name__ == '__main__':
    main()
