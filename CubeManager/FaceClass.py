class Face:
    def __init__(self, color, orient, face_list = None):
        self.color = color
        self._top = False
        self._right = False
        self._left = False
        self._front = False
        self._back = False
        self._bottom = False
        self.set_orientation(orient)

        if not face_list:
            self.face_list = [[color for i in range(3)],
                              [color for i in range(3)],
                              [color for i in range(3)]]
        else:
            self.face_list = face_list

    # Getters
    def get_right_row(self):
        right_row = []
        for i in self.face_list:
            right_row.append(i[len(i)-1])
        return right_row

    def get_left_row(self):
        left_row = []
        for i in self.face_list:
            left_row.append(i[0])
        return left_row

    def get_top_row(self):
        return self.face_list[0]

    def get_bottom_row(self):
        return self.face_list[len(self.face_list) - 1]

    def get_middle_row_h(self):
        """
        Returns the horizontal middle row
        [[A, B, C],
         [E, F, G],   --------> [E, F, G]
         [H, I, K]]
        """
        return self.face_list[1]

    def get_middle_row_v(self):
        """
        Returns the vertical middle row
        [[A, B, C],
         [E, F, G],   --------> [B, F, I]
         [H, I, K]]
        """
        temp_middle_row = [self.face_list[0][1], self.face_list[1][1], self.face_list[2][1]]
        return temp_middle_row

    def get_corners(self):
        """
        Returns the value of corners in a list in this format
        [[A, B, C],
         [E, F, G],   --------> [A, C, K, H]
         [H, I, K]]
        """
        corner_list = [self.face_list[0][0], self.face_list[0][2], self.face_list[2][2], self.face_list[2][0]]
        return corner_list

    def get_edges(self):
        """
        Returns the value of edges in a list in this format

        [[A, B, C],
        [E, F, G],   --------> [E, B, G, I]
        [H, I, K]]
        """

        edge_list = [self.face_list[1][0], self.face_list[0][1], self.face_list[1][2], self.face_list[2][1]]
        return edge_list

    def __str__(self):
        return f'{self.face_list[0]}\n{self.face_list[1]}\n{self.face_list[2]}'

    # Setters
    def set_right_row(self, new_right_row):
        new_right_row = list(new_right_row)
        for index, i in enumerate(self.face_list):
            i[len(i)-1] = new_right_row[index]
        return self.get_right_row()

    def set_left_row(self, new_left_row):
        new_left_row = list(new_left_row)
        for index, i in enumerate(self.face_list):
            i[0] = new_left_row[index]
        return self.get_left_row()

    def set_top_row(self, new_top_row):
        new_top_row = list(new_top_row)
        self.face_list[0] = new_top_row
        return self.get_top_row()

    def set_bottom_row(self, new_bottom_row):
        new_bottom_row = list(new_bottom_row)
        self.face_list[len(self.face_list) - 1] = new_bottom_row
        return new_bottom_row

    def set_orientation(self, orientation):
        match orientation:
            case "top":
                self._top = True
            case "bottom":
                self._bottom = True
            case "front":
                self._front = True
            case "back":
                self._back = True
            case "left":
                self._left = True
            case "right":
                self._right = True

    def set_corners(self, new_corners_list):

        """
        Sets the values of corners in this format:
                                      [[A, 0, C],
        [A, C, K, H] ------------->    [0, 0, 0],
                                       [H, 0, K]]
        """

        self.face_list[0][0] = new_corners_list[0]
        self.face_list[0][2] =  new_corners_list[1]
        self.face_list[2][2] = new_corners_list[2]
        self.face_list[2][0] = new_corners_list[3]

    def set_middle_row_h(self, new_middle_row_h):
        """
        Sets the values of middle row horizontally via list in this format:
                                     [[0, 0, 0],
        [E, F, G]   ------------->    [E, F, G],
                                      [0, 0, 0]]
        """
        self.face_list[1] = new_middle_row_h
        return

    def set_middle_row_v(self, new_middle_row_v):
         """
         Sets the values of middle row horizontally via list in this format:
                                      [[0, B, 0],
         [B, F, I]   ------------->    [0, F, 0],
                                       [0, I, 0]]
         """
         self.face_list[0][1] = new_middle_row_v[0]
         self.face_list[1][1] = new_middle_row_v[1]
         self.face_list[2][1] = new_middle_row_v[2]
         return
    
    def set_edges(self, new_edges):
        """
        Sets the value of edges via a list in this format:
                                    [[0, B, 0],
        [E, B, G, I]   -------->     [E, F, G],
                                     [0, I, 0]]
        """
        self.face_list[1][0] = new_edges[0]
        self.face_list[0][1] = new_edges[1]
        self.face_list[1][2] = new_edges[2]
        self.face_list[2][1] = new_edges[3]
        return
