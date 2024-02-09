from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    
    def get_solution(self):
        L=[]
        for i in range (self.n*self.m):
            a,b=find(i)
            if i%self.m==0: #cas particulier si "i" doit aller tout à droite
                L+=get_swap_droite(a,b,self.m-b) #faire self.m-b swap à droite
            if i%self.m<b:   
                L+=get_swap_gauche(a,b,b-(i%self.m)) #faire position moins reste swaps à gauche
            if i%self.m>b:
                L+=get_swap_droite(a,b,i%self.m-b) #faire reste moins positions swaps à droite
            if i//self.n+1<a:
                L+=get_swap_haut(a,b,a-(i//self.n+1)) #faire position moins quotient swaps en haut
        swap_seq(L)
        return(L)
            
                      
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        #raise NotImplementedError

