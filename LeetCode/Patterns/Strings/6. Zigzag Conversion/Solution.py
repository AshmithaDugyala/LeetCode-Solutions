class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        rows=[""]*numRows
        row=0
        go_down=False
        for i in s:
            rows[row]+=i
            if row==numRows-1:
                go_down=False
            elif row==0:
                go_down=True
            if go_down==True:
                row+=1
            elif go_down==False:
                row-=1
        return "".join(rows)