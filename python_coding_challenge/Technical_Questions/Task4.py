# Writing  a  well-documented  code  creates  a  function  that calculates simple interest

def simple_interest(P, T, R):
     """ P = principal
         T = Time
         R= Rate"""
     SI = (P * T * R) / 100
     print(SI)


simple_interest(100, 5, 4)
