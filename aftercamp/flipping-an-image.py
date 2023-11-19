class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = []
        for line in image:
            new = []
            for idx in range(len(line) - 1, -1, -1):
                if line[idx] == 1:
                    new.append(0)
                else:
                    new.append(1)

            new_image.append(new)

        return new_image

        