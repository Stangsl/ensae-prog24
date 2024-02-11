from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    #A first solving method that finds every int "i" in [1;n*m] and puts "i" to its place then "i"+1 ... so that there are only right or left swaps depending on where "i" is found and then it remains only swaps to the top to fix "i" to its place.
    @staticmethod
    def get_solution(grid):
        L=[]
        for i in range (grid.n*grid.m):
            a, b=grid.find(i)
            if i%grid.m==0: #particular case if "i" needs to go all to the right
                L+=grid.get_swap_droite(a,b,grid.m-b) #perform self.m-b swap to the right
            if i%grid.m<b:   
                L+=grid.get_swap_gauche(a,b,b-(i%grid.m)) #perform "position" - "rest" swaps to the left
            if i%grid.m>b:
                L+=grid.get_swap_droite(a,b,i%grid.m-b) #perform "rest" - "position" swaps to the right
            if i//grid.n+1<a:
                L+=grid.get_swap_haut(a,b,a-(i//grid.n+1)) #perform "position" - "i//grid.n+1" swaps to the top to achieve "i"'s positioning
        return(L)
            
                      
        """
        This method ALWAYS solves the grid (by using swap_seq to the sequence "L") and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...] in a O((n*m)*(n+m)) TIME COMPLEXITY that we deduced implementig a "k" variable that becomes "k+=1" for every pass through the for loops ... This methods is of course not optimal.
        """
