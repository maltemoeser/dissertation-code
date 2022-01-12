import numpy as np
from itertools import zip_longest

X_dtypes = {
    "optimal_change": np.int8,
    "optimal_change_with_fee": np.int8,
    "address_type": np.int8,
    "power_of_ten_2": np.int8,
    "power_of_ten_3": np.int8,
    "power_of_ten_4": np.int8,
    "power_of_ten_5": np.int8,
    "power_of_ten_6": np.int8,
    "power_of_ten_7": np.int8,
    "fp_inout_count": np.int8,
    "fp_output_count": np.int8,
    "fp_version": np.int8,
    "fp_locktime": np.int8,
    "fp_rbf": np.int8,
    "fp_segwit": np.int8,
    "fp_possible_segwit": np.int8,
    "fp_ordered_inouts": np.int8,
    "fp_zeroconf": np.int8,
    "fp_multisig": np.int8,
    "fp_address_type": np.int8,
    "fp_multisig": np.int8,
    "fp_p2pkh": np.int8,
    "fp_p2wpkh": np.int8,
    "fp_p2sh": np.int8,
    "fp_p2wsh": np.int8,
    "fp_absolute_fee": np.int8,
    "fp_relative_fee": np.int8,
    "co_output_value": np.uint64,
    "co_is_larger_output": np.bool,
    "co_fresh_output": np.bool,
    "co_other_fresh": np.bool,
    "co_output_value_ratio": np.float64,
    "co_output_index": np.uint8,
    "ct_fee": np.uint64,
    "ct_fee_per_byte": np.uint64,
    "ct_tx_value": np.uint64,
    "ct_segwit_tx": np.uint8,
    "ct_version": np.uint64,
    "ct_has_locktime": np.bool,
    "ct_block_height": np.uint32,
    "ct_input_count": np.uint32,
}

def get_X_dtypes():
    return X_dtypes

def get_base_path(ext=""):
    if ext[:1] == "/":
        ext = ext[1:]
    return "/n/fs/scratch/mmoeser/2021/" + ext

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)