import re
import numpy as np

# import copy

def run_if_true(bool_run, func, *args, **kwargs):
    if bool_run:
        func(*args, **kwargs)

def print_shape(shape, verbose):
    for row in shape:
        run_if_true(verbose, print, " ".join([("#" if i else ".") for i in row.tolist()]))

def print_region(shape, verbose):
    for row in shape:
        run_if_true(verbose, print, " ".join([("X" if i else ".") for i in row.tolist()]))


def shape_to_string(sh):
    return "".join(["#" if s else "." for s in sh.flatten().tolist()])

def string_to_shape(s):
    return (np.array(list(s)) == "#").reshape((3, 3))

def main():
    fn = "inputs/aoc-25-dec-12.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    verbose_1 = False
    verbose_2 = True
    # verbose = True

    shapes = {}
    regions = []

    line_idx = 0
    while line_idx < len(lines):
        cur_line = lines[line_idx]
        run_if_true(verbose_1, print, cur_line)
        # exit(0)

        # read shape
        if match := re.fullmatch(pattern="([0-9]+)\\:", string=cur_line):

            shape_idx = int(match.group(1))

            shape = ""

            line_idx += 1
            while (cur_line := lines[line_idx]) != "":
                shape += cur_line
                line_idx += 1

            shapes[shape_idx] = {
                "base": shape,
                "options": set(shape),
                "area": sum([1 if ch == "#" else 0 for ch in shape])
            }
            # shapes[shape_idx] = np.array(shape)

        if match := re.fullmatch(
            pattern="([0-9]+)x([0-9]+)\\:((?: [0-9]+)+)",
            string=cur_line
        ):
            region = {}

            region["shape"] = (int(match.group(2)), int(match.group(1)))
            region["quantity_per_shape"] = []
            # for i in range(2, len(match_groups)):
            #     region["quantity_per_shape"].append(int(match_groups[i]))

            for i in match.group(3).strip().split(" "):
                region["quantity_per_shape"].append(int(i))

            regions.append(region)

        line_idx += 1


    # add np matrix and all posisble variants 
    for sn in shapes.keys():

        run_if_true(verbose_1, print, f"New shape: {sn}")
        run_if_true(verbose_1, print, f"area: {shapes[sn]['area']}")
        # shapes[sn]["options"] = []

        # options = []
        # base_option = shapes[sn]["base"]
        # base_option = np.array(base_option)
        # base_option = (base_option == "#")

        # options.append(base_option)

        base_option = string_to_shape(shapes[sn]["base"])

        # print_shape(base_option)
        # run_if_true(verbose, print, )

        # print_shape(np.fliplr(base_option))
        # exit(0)

        options = [base_option, ]

        for _ in range(3):
            options.append(np.rot90(options[-1]))

        for i in range(len(options)):
            options.append(np.fliplr(options[i]))

        # run_if_true(verbose, print, len(options))
        options = set([shape_to_string(o) for o in options])
        for o in set(options):
            print_shape(string_to_shape(o), verbose_1)
            run_if_true(verbose_1, print, "")


        shapes[sn]["options"] = options
        # run_if_true(verbose, print, base_option)
        # run_if_true(verbose, print, shape_to_string(base_option))
        # run_if_true(verbose, print, string_to_shape(shape_to_string(base_option)))
        # print_shape(base_option)
        # run_if_true(verbose, print, )

        # print_shape(np.rot90(base_option))
        # run_if_true(verbose, print, )

        # exit(0)




    # import json
    # run_if_true(verbose, print, json.dumps(shapes, indent=2))
    # run_if_true(verbose, print, )
    # run_if_true(verbose, print, json.dumps(regions, indent=2))

    total_successful_fit = 0
    # for region in regions[2:3]:
    # for region in regions[2:3]:
    # for region in regions[0:1]:
    # for region in regions[1:2]:
    # for region in regions[:2]:
    for region_id, region in enumerate(regions[:]):
        run_if_true(verbose_2, print, f"Current region {region_id} with shape  {region['shape']}")
        region_map = np.full((region["shape"]), False)

        shapes_to_fit = []
        for shape_idx, shape_quantity in enumerate(
            region["quantity_per_shape"]
        ):
            for _ in range(shape_quantity):
                shapes_to_fit.append(shape_idx)

        total_shape_area = sum([shapes[s]["area"] for s in shapes_to_fit])
        region_area = region["shape"][0] * region["shape"][1]
        if total_shape_area > region_area:
            run_if_true(verbose_1, print, "region area is too small, skip fitting")
            continue

        call_cache = {}
        def try_to_fit(stf, rm) -> bool:
            run_if_true(verbose_1, print, "Start iteration")
            run_if_true(verbose_1, print, stf)
            print_region(rm, verbose_1)

            call_signature = ""
            call_signature += shape_to_string(rm)
            call_signature += "".join(map(str, stf))

            if call_signature in call_cache:
                run_if_true(verbose_1, print, "Hit the cache!, return")
                return call_cache[call_signature]

            if not stf:

                call_cache[call_signature] = True
                return True

            area_left = (~rm).sum()
            if area_left < shapes[stf[0]]["area"]:
                run_if_true(verbose_1, print, "exit, area not enough for current fit")
                call_cache[call_signature] = False
                return False

            if area_left < sum([shapes[s]["area"] for s in stf]):
                run_if_true(verbose_1, print, "exit, area not enough for all other fits")
                call_cache[call_signature] = False
                return False

            s = stf.pop(0)

            # if (~rm).sum() < shapes[s]["area"]:
            #     run_if_true(verbose, print, "exit, area not enough")
            #     return false

            shape_dim = string_to_shape(shapes[s]["base"]).shape
            for i in range(rm.shape[0] - shape_dim[1] + 1):
                for j in range(rm.shape[1] - shape_dim[0] + 1):

                    # run_if_true(verbose, print, i, j)
                    # if not occupied
                    if not rm[i, j]:
                        box_to_fit_in =  rm[
                            i: i+shape_dim[0],
                            j: j+shape_dim[1]
                        ] 

                        if (~box_to_fit_in).sum() < shapes[s]["area"]:
                            continue

                        for ss_str in shapes[s]["options"]:
                            ss = string_to_shape(ss_str)

                            run_if_true(verbose_1, print, "Try to fit:")
                            print_shape(ss, verbose_1)

                            overlap = box_to_fit_in.astype(int) \
                                    + ss.astype(int)
                            if overlap.max()  <= 1:
                                run_if_true(verbose_1, print, f"Fitted {i} {j}")
                                updated_rm = rm.copy()
                                updated_rm[
                                    i: i+shape_dim[0],
                                    j: j+shape_dim[1]
                                ] = updated_rm[
                                    i: i+shape_dim[0],
                                    j: j+shape_dim[1]
                                ] | ss

                                if try_to_fit(stf[:], updated_rm):
                                    call_cache[call_signature] = True
                                    return True
                            else:
                                run_if_true(verbose_1, print, f"Not fitted {i} {j}")

            call_cache[call_signature] = False
            return False

        if try_to_fit(shapes_to_fit, region_map):
            total_successful_fit += 1

            run_if_true(verbose_2, print, "Region could be fitted with shapes")
        else:
            run_if_true(verbose_2, print, "Region could not be fitted with shapes")

    print()
    print(f"Total fitted regions: {total_successful_fit}")







        # run_if_true(verbose, print, shapes_to_fit)
        # run_if_true(verbose, print, region["quantity_per_shape"])
        # print_region(region_map)










if __name__ == "__main__":
    main()
