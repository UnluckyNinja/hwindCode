import sys
from evaluate_model import evaluateParam

if (__name__ == "__main__"):
    if (len(sys.argv) == 2):
        file_mode = "local"
        file_path = sys.argv[1]
    elif (len(sys.argv) == 3 and sys.argv[1].lowercase == "azure"):
        file_mode = "azure"
        file_path = sys.argv[2]
    else:
        print("Usage: local_evaluatin.py [azure] file_name|azure_file_guid")
        sys.exit(0)

    items = []
    if (file_mode == "local"):
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                cols = line.split('\t')
                items.append((cols[0], cols[1], cols[2], cols[3], cols[4]))
    else:
        print("To do: add azure file support")
        sys.exit(0)

    multi_mode = False
    if (multi_mode == True):
        low_bar_start = -0.2
        high_bar_start = 0.2
        ratio_start = 1.1
        max_value = 0
        max_combine = "nothing"

        for i in range(0, 5):
            low_bar = low_bar_start + 0.005*i
            for j in range(0, 5):
                high_bar = high_bar_start + 0.005*j
                for k in range(0, 2):
                    ratio = ratio_start + 0.1*k
                    param = (low_bar, high_bar, ratio)
                    run_result = evaluateParam(param, items, False)
                    if (max_value < run_result[0]):
                        max_value = run_result[0]
                        max_combine = "{0}_{1}_{2}".format(low_bar, high_bar, ratio)
        print(max_value)
        print(max_combine)
    else:
        param = (-0.18, 0.19, 19.6)
        run_result = evaluateParam(param, items, True)
        print(run_result)