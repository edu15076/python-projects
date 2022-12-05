from inspect import _void

def quick_sort(li:list, start = 0, end = None):
    def partition(li, start, end):
        count = start
        piv = li[end]
        for i in range(start, end):
            if li[i] <= piv:
                li[i], li[count] = li[count], li[i]
                count += 1
        li[end], li[count] = li[count], li[end]
        return count
    
    if end == None: end = len(li) - 1

    if start < end:
        ciner_index = partition(li, start, end)
        quick_sort(li, start, ciner_index - 1)
        quick_sort(li, ciner_index + 1, end)
