import pandas as pd
import numpy as np
import blocksci

def assess_accuracy(predicted, actual):
    correct = 0
    incorrect = 0
    unidentified = 0
    
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    
    assert len(predicted) == len(actual)
    
    for predicted_value, actual_value in zip(predicted, actual):
        if predicted_value == -1:
            unidentified += 1
            fn += 1
            tn += 1
        elif predicted_value == actual_value:
            correct += 1
            tp += 1
            tn += 1
        else:
            incorrect += 1
            fp += 1
            fn += 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    print(round(precision, 6), "&", round(recall, 6), "&")
    print("Heuristic identified a unique change output in {}% of transactions.".format(round((correct + incorrect)/len(actual)*100, 2)))
    print("Heuristic was correct for {}% of identified change outputs.".format(round(correct/(correct + incorrect) * 100, 2)))
    return {"correct": correct, "incorrect": incorrect, "unindentified": unidentified}

def df_accuracy_over_time(predicted, actual, timestamps):
    result = []
    ts = []
    for predicted_value, actual_value, timestamp in zip(predicted, actual, timestamps):
        if predicted_value == -1:
            continue
        else:
            result.append(int(predicted_value == actual_value))
            ts.append(timestamp)
    assert len(result) == len(ts)
    return pd.DataFrame({"Correct": result}, index=ts)

def output_characteristics():
    return {
        "co_output_value": (lambda txes: txes.outputs.value, np.uint64),
        "co_is_larger_output": (lambda txes: txes.outputs.map(lambda o: o.tx.outputs.max(lambda x: x.value).map(lambda x: x.index).or_value(99) == o.index), np.bool),
        "co_output_index": (lambda txes: txes.outputs.index, np.uint8),
        
    }

def output_value_ratio():
    return {
        "co_output_value_ratio": (lambda output_value, tx_value: output_value/tx_value, np.float64),
    }

def tx_characteristics():
    return {
        "ct_fee": (lambda txes: txes.outputs.map(lambda o: o.tx.fee), np.uint64),
        "ct_fee_per_byte": (lambda txes: txes.outputs.map(lambda o: o.tx.fee_per_byte()), np.uint64),
        "ct_tx_value": (lambda txes: txes.outputs.map(lambda o: o.tx.output_value), np.uint64),
        "ct_segwit_tx": (lambda txes: txes.outputs.map(lambda o: o.tx.segwit), np.uint8),
        "ct_has_locktime": (lambda txes: txes.outputs.map(lambda o: blocksci.heuristics.has_locktime(o.tx)), np.bool),
        "ct_version": (lambda txes: txes.outputs.map(lambda o: o.tx.version), np.uint64),
        "ct_block_height": (lambda txes: txes.outputs.map(lambda o: o.tx.block.height), np.uint32),
        "ct_input_count": (lambda txes: txes.outputs.map(lambda o: o.tx.input_count), np.uint32),
    }

