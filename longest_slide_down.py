def longest_slide_down(pyramid):
    # TODO: write some code...

    for i in range(len(pyramid)-2,-1,-1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] = pyramid[i][j] + max(pyramid[i+1][j], pyramid[i+1][j+1])
        pyramid.pop()
        
    return pyramid[0][0]