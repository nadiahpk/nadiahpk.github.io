#***************************************************************************** 
#       Copyright (C) 2009 Nadiah Kristensen <nadiah.kristensen@gmail.com>   #
#                                                                            # 
#  Distributed under the terms of the GNU General Public License (GPL)       #
#                                                                            # 
#                  http://www.gnu.org/licenses/                              #
#*****************************************************************************

"""
Handy for debugging:
import IPython
IPython.Shell.IPShell(user_ns=dict(globals(), **locals())).mainloop()
"""

import scipy
from numpy import *
from numpy.fft import *
import copy
#import matplotlib.pyplot as plt
import cPickle
from random import choice # For choosing random from web

# ------------------------------------
def get_M(file_name):
    M_file = open(file_name, 'r')
    spare = M_file.readlines()
    K = len(spare)
    M = scipy.zeros((K,K),float)
    for i in range(0,K):
        row = spare[i]
        row = row.split()
        for j in range(0,K):
            #print '(' + str(i) + ',' + str(j) + ')'
            M[i,j] = float(row[j])
    M_file.close()

    return M

# Create a new random M
def create_M(K):
    M = scipy.zeros((K,K),float)
    for i in range(0,K-1):
        for j in range(i+1,K):
            M[i,j] = random.normal()
            M[j,i] = -M[i,j]
    return M

# Extend M to double the size, or add L entries
def extend_M(M,L=None):
    K = len(M)
    if L == None:
        newK = 2*K
    else:
        newK = K+L

    exM = scipy.zeros((newK,newK),float)
    for i in range(0,newK-1):
        for j in range(i+1,newK):
            if (i < K) and (j < K):
                exM[i,j] = M[i,j]
                exM[j,i] = M[j,i]
            else:
                exM[i,j] = random.normal()
                exM[j,i] = -exM[i,j]
    return exM

# Define traits for a member taken from the second half of the M matrix
def create_novel_traits(K,L=10):
    traits = []
    while len(traits) < L:
        new_trait = random.randint(K/2,K)
        if new_trait not in traits:
            traits.append(new_trait)
    return sort(traits)

# Define traits for a member
def create_traits(K, L):
    traits = []
    while len(traits) < L:
        new_trait = random.randint(0,K)
        if new_trait not in traits:
            traits.append(new_trait)
    return sort(traits)

# Returns the fid after you've found the string stop_str
def findstr(fid,stopstr):
    stopflag = False
    while stopflag == False:
        v = fid.readline().split()
        if len(v) != 0:
            if len(v[0]) > len(stopstr):
                if v[0][0:len(stopstr)] == stopstr:
                    stopflag = True

    return fid

# Get a web from an octave file
def get_web(file_name,params):
    web = Web() # Initialise web
    # Read in web, file_name = 'egweb.m'
    fid = open(file_name,'r')

    # Read in traits of each species
    # The first entry will be 'featVec?? = something', so search for that
    fid = findstr(fid,'featVec')
    # The next line will be the traits of the resource, and then the traits of each species after that
    # It will end when we hit '];'
    trait_d = {}
    counter = 0
    v = fid.readline().split()
    while v[0] != '];':
        for i in range(0,len(v)): # Convert strings to integers
            v[i] = int(v[i])
        v = sort(v)
        # Append to dict of traits
        trait_d[counter] = v
        v = fid.readline().split()
        counter += 1

    # Create members with id taken from idVec
    # The next entry will be 'idVec?? = something', so search for that
    fid = findstr(fid,'idVec')
    # The first one is the resource
    v = fid.readline().split()
    v = int(v[0]) #assert v == 0 ***
    web[v] = Member(params, id = v, traits = trait_d[v], type = 'resource')
    # There should be as many members in idVec as there are in traits_d
    for i in range(1,len(trait_d)):
        v = fid.readline().split()
        v = int(v[0])
        web[i] = Member(params, id = v, traits = trait_d[i]) # For now, the web key will be the order

    # Skip the parentage for now

    # Assign n values
    # The next entry will be 'nVec?? = something', so search for that
    fid = findstr(fid,'nVec')
    # The n values are on a single line
    v = fid.readline().split()
    for i in range(0,len(web)):
        web[i].n = float(v[i])

    # Assign S values
    fid = findstr(fid,'S')
    for i in range(0,len(web)):
        v = fid.readline().split()
        for j in range(0,len(web)):
            sij = float(v[j])
            if sij > 0:
                web[i].S[web[j].id] = sij

    # Assign F values
    fid = findstr(fid,'F')
    for i in range(0,len(web)):
        v = fid.readline().split()
        for j in range(0,len(web)):
            fij = float(v[j])
            if fij > 0:
                web[i].F[web[j].id] = fij

    # Assign G values
    fid = findstr(fid,'G')
    for i in range(0,len(web)):
        v = fid.readline().split()
        for j in range(0,len(web)):
            gij = float(v[j])
            if gij > 0:
                web[i].G[web[j].id] = gij

    # Assign A values
    fid = findstr(fid,'A')
    for i in range(0,len(web)):
        v = fid.readline().split()
        for j in range(0,len(web)):
            aij = float(v[j])
            if aij > 0:
                web[i].A[web[j].id] = aij

    # Make the id values the keys to the web
    tempweb = Web()
    for i in web:
        tempweb[web[i].id] = web[i]

    fid.close()

    return tempweb

class Web(dict):
    def initialise(self,params,M):
        b = params['b']
        lam = 0.1 # Parameter from Drossel et al. (2001)

        # Create web
        #web = {}

        # Create resource
        res = Member(params,type = "resource")
        self[res.id] = res

        # Create first invader and add to web
        self.add_random_member(params)

        # Update S
        self.update_S(M)

        # Use s of single invader to find n. This is peculiar to the
        # one-resource one-species system
        invader_id = max(self.keys())
        if (self[invader_id].S).has_key(res.id):
            s = self[invader_id].S[res.id]
            self[invader_id].n = (lam*s-b)*res.n/s
        else:
            self[invader_id].n = 0
        while self[invader_id].n < 1: # Keep repeating the above until we have a viable first species
            self.pop(invader_id)
            self.add_random_member(params,prev_id = invader_id)
            self.update_S(M)
            invader_id = max(self.keys())
            if (self[invader_id].S).has_key(res.id):
                s = self[invader_id].S[res.id]
                self[invader_id].n = (lam*s-b)*res.n/s
            else:
                self[invader_id].n = 0

        invader = self[invader_id] # Pointer to invader in web
        # Make it so the first species concentrates all of its effort on
        # the resource
        invader.F[res.id] = 1

        # Calculate G (equation 4, special case for single species)
        invader.G[res.id] = (invader.S[res.id]*res.n) / (b*res.n + invader.S[res.id]*invader.n)

    def add_random_member(self, params, prev_id = None):
        if prev_id == None:
            prev_id = max(self.keys())
        invader = Member(params,prev_id = prev_id)
        while self.has_member(invader):
            prev_id += 1
            invader = Member(params,prev_id = prev_id)
        self[invader.id] = invader

    # Check if member invader is in the web
    def has_member(self, invader):
        answer = False
        for id in self:
            if self[id] == invader:
                answer = True # Member invader is in web
        return answer

    def update_S(self,M): # Update S
        L = 10 # Same as Drossel et al. (2001)

        invader_id = max(self.keys())
        for native_id in self:
            if native_id != invader_id:
                s = 0
                for alpha in self[native_id].traits:
                    for beta in self[invader_id].traits:
                        # Equation 1 sum
                        s += M[alpha,beta]

                if s > 0: # Equation 1 sum divided by L
                    if self[native_id].type == 'species':
                        self[native_id].S[invader_id] = s/L
                else:
                    self[invader_id].S[native_id] = -s/L

    # Return a mutant offspring
    def mutant_offspring(self,K):
        L = 10 # Same as Drossel et al. (2001)

        offspring = self.rand() # Initialise offspring as equal to its parent
        new_trait = random.randint(0,K) # Choose a new trait that is not in the offspring's traits
        while new_trait in offspring.traits:
            new_trait = random.randint(0,K)
        # Now choose a random trait to replace with it
        offspring.traits[random.randint(0,L)] = new_trait
        offspring.traits = sort(offspring.traits)
        # Initialise all of its properties
        offspring.lineage['parent'] = offspring.id # Currently equal to parent's id
        # offspring.lineage['firstancestor'] stays the same
        offspring.lineage['mutnage'] += 1
        offspring.n = 1
        offspring.A = {}
        #offspring.A[offspring.id] = 1
        offspring.F = {}
        offspring.oldF = {}
        offspring.G = {}

        return offspring

    # Add a unique mutant offspring to the web
    def add_offspring(self,id,K):
        # Create an offspring
        # Choose random parent and make offspring equal it
        offspring = self.mutant_offspring(K)
        while self.has_member(offspring): # While the offspring is in the web
            offspring = self.mutant_offspring(K)
        offspring.id = id
        self[offspring.id] = offspring

    # Return a random species
    def rand(self):
        id = self.keys()[random.randint(1,len(self))]
        
        return copy.deepcopy(self[id])

    def update_A(self,c):
        invader = self[max(self.keys())]
        for id in self:
            member2 = self[id]
            if invader.id == id:
                invader.A[id] = 1
            else:
                if (member2.type == 'species'):
                    invader.A[id] = invader.calc_a(member2,c)
                    member2.A[invader.id] = invader.A[id]

    # Initialise feeding efforts f
    def init_F(self):
        initial_f = 1e-6 # Start fij at this value

        for k in self:
            member = self[k] # Pointer
            for j in member.S:
                if member.F.has_key(j):
                    if member.F[j] < initial_f:
                        member.F[j] = initial_f
                else:
                    member.F[j] = initial_f

    # Update G
    def update_G(self,b):

        for i in self:
            member = self[i] # pointer to pred
            for j in member.F: # prey
                compn = 0
                for k in self: # each potential competitor
                    if self[k].F.has_key(j): # if it is a competitor
                        #print '(' + str(i) + ',' + str(j) + ',' + str(k) + ')'
                        # Equation 13 sum
                        compn += self[k].A[i]*self[k].S[j]*self[k].F[j]*self[k].n
                # Equation 13 complete
                member.G[j] = (member.S[j]*member.F[j]*self[j].n)/(b*self[j].n+compn)

    # Update F
    def update_F(self):
        initial_f = 1e-6 # Start fij at this value

        for i in self:
            member = self[i] # Pointer to i
            sumg = 0
            for k in member.G: # Get sum g_ik
                sumg += member.G[k]
            list_rem = []
            for j in member.F:
                member.F[j] = member.G[j]/sumg # Equation 14
                if member.F[j] < initial_f:
                    list_rem.append(j)
            for j in list_rem:
                member.F.pop(j)

    # Update oldF - that is, make oldF equal F
    def update_oldF(self):
        for i in self:
            member = self[i] # Pointer to species
            member.oldF = {}
            for j in member.F:
                member.oldF[j] = member.F[j] # Deep copy

    # Iteratively solve for F and G
    def equilibriate_FG(self,b):
        del_f_cutoff = 0.1 # Percentage change in F before we say it's equilibriated
        self.init_F() # Set small values of F to something
        # Find del_f_max
        del_f_max = del_f_cutoff + 1
        while del_f_max > del_f_cutoff:
            # Update F and G
            self.update_oldF()
            self.update_G(b)
            self.update_F()
            # Find the maximum proportional change in F, del_f_max
            del_f_max = 0
            for i in self:
                member = self[i] # Pointer to species
                for j in member.oldF:
                    if member.F.has_key(j):
                        del_f = abs(member.oldF[j]-member.F[j])/member.oldF[j]
                    else:
                        del_f = 1 # Because F = 0
                    if del_f > del_f_max:
                        del_f_max = del_f

    # Find losses and gains (sum_i n_i g_ij and sum_j n_j g_ji in Equation 3)
    def gains_losses(self):
        gains = {}
        losses = {}
        # Find losses and gains (sum_i n_i g_ij and sum_j n_j g_ji in Equation 3)
        for i in self:
            member = self[i]
            for j in member.G:
                flow = member.G[j]*member.n
                if gains.has_key(i):
                    gains[i] += flow
                else:
                    gains[i] = flow
                if losses.has_key(j):
                    losses[j] += flow
                else:
                    losses[j] = flow
        return [gains,losses]
        
    # Do one Euler time-step, returns maximum change in n
    def eulerstep(self,del_t):
        lam = 0.1 # Parameter from Drossel et al. (2001)

        # Find losses and gains (sum_i n_i g_ij and sum_j n_j g_ji in Equation 3)
        [gains,losses] = self.gains_losses()
        # Update steady state ...
        del_n_max = 0 # ... and record maximum change in population
        extinct = []
        for i in self:
            # Take out gain and loss for each member
            member = self[i]
            if member.type == 'species':
                if gains.has_key(i):
                    gain = gains[i]
                else:
                    gain = 0
                if losses.has_key(i):
                    loss = losses[i]
                else:
                    loss = 0
                del_n = member.n # Record previous value of n
                # Equation 3
                member.n += del_t*(-member.n + lam*gain - loss) 
                del_n = abs(del_n - member.n)
                if del_n > del_n_max:
                    del_n_max = del_n # Record largest change in population
                # If species has died out, add to extinct list
                if member.n < 1:
                    extinct.append(i)
        # Remove extinct species
        for i in extinct:
            self.remove(i)

        return del_n_max

    # Remove member i from the web, including all references to i
    def remove(self,i):
        self.pop(i)
        for j in self:
            member = self[j]
            if member.F.has_key(i):
                member.F.pop(i)
            if member.A.has_key(i):
                member.A.pop(i)
            if member.G.has_key(i):
                member.G.pop(i)
            if member.S.has_key(i):
                member.S.pop(i)
        

    # Equilibriate web
    def equilibriate(self,euler_params,params,inv_id=None):
        del_t = euler_params['del_t'] 
        t_max = euler_params['t_max'] 
        eqm_tol = euler_params['eqm_tol'] 
        b = params['b']

        t_count = 0
        del_n_max = eqm_tol + 1
        if inv_id == None:
            while (del_n_max > eqm_tol) and (t_count < t_max):
                self.equilibriate_FG(b)
                del_n_max = self.eulerstep(del_t)
                t_count += 1
        else: # When testing invasion, only need to see if it drops out
            while (del_n_max > eqm_tol) and (t_count < t_max) and (self.has_key(inv_id)):
                self.equilibriate_FG(b)
                del_n_max = self.eulerstep(del_t)
                t_count += 1

    # Plot populations forward by t_final with step size del_t
    def plot(self,params,t_final,del_t):
        b = params['b']
        n = {}
        for i in self:
            n[i] = [self[i].n]
        for t in range(0,t_final):
            self.equilibriate_FG(b)
            del_n_max = self.eulerstep(del_t)
            for i in self:
                n[i].append(self[i].n)
        # Plotting
        for i in self:
            if self[i].type == 'species':
                leg = 'Spp ' + str(i)
                plt.plot(n[i],label=leg)
        plt.title('Species population versus time')
        plt.xlabel('Time')
        plt.ylabel('Population')
        #plt.legend()
        plt.show()

    # Make dotty file
    def dottify(self,file_name = 'test.dot',f_cutoff = 0.01):
        fid = open(file_name,'w')
        fid.write('# To create figure: dot -Tps file_name.dot > file_name.ps\n')
        fid.write('digraph foodweb { \n');
        fid.write('   rankdir=BT; \n');
        fid.write('   node [shape = circle]; \n');
        for i in self:
            member = self[i]
            for j in member.F:
                if member.F[j] > f_cutoff:
                    fid.write('  %s -> %s [style=\"setlinewidth(%s)\"]; \n' % (j, i, 2*(round(100*member.F[j]-f_cutoff+.01))/100))
        fid.write('}\n');
        fid.close()

    # Returning values from the web
    def ret_n(self):
        n = {}
        for i in self:
            n[i] = web[i].n
        return n

    # Get all of the attributes (returned in a list) that we are doing the single mediations on
    def get_atts(self,f_cutoff = 0.01):
        sz = len(self) - 1

        # Save the link structure ...
        link_from = [] # Checked
        link_to = []
        # Attribute: meanS
        meanS = 0 # Checked
        count = 0
        for i in self:
            member = self[i]
            for j in member.F:
                #if self[j].id != 0 and member.F[j] > f_cutoff: FIX AT END TO THIS
                if member.F[j] > 0.01: # Set for consistency with previous
                    meanS += member.S[j]
                    count += 1
                    if self[j].id != 0 and member.F[j] > 0.1: # Again, for consistency with previous ***
                        link_to.append(i)
                        link_from.append(j)
        meanS = float(meanS)/count

        # Attribute: Connectance
        C = float(len(link_from))/(sz*(sz-1)) # Same as Loueille 

        # Attribute: trophic fractions. Count basal, intermediate, and top species Checked
        basal = 0
        intermediate = 0
        top = 0
        trophic_type = {}
        for i in self:
            member = self[i]
            if member.type == 'species':
                if (member.id in link_to) == False:
                    trophic_type[member.id] = 'basal'
                    basal += 1
                elif (member.id in link_from) == False:
                    trophic_type[member.id] = 'top'
                    top += 1
                else:
                    trophic_type[member.id] = 'intermediate'
                    intermediate += 1
        basal = float(basal)/sz
        intermediate = float(intermediate)/sz
        top = float(top)/sz
        # Take logs *** move later
        #basal = log(basal/(1-basal))
        #intermediate = log(intermediate/(1-intermediate))
        #top = log(top/(1-top))

        # Attribute: link-type fractions Checked
        bi = 0
        bt = 0
        ii = 0
        it = 0
        for i in range(0,len(link_from)):
            if trophic_type[link_from[i]] == 'basal':
                if trophic_type[link_to[i]] == 'intermediate':
                    bi += 1
                elif trophic_type[link_to[i]] == 'top':
                    bt += 1
            elif trophic_type[link_from[i]] == 'intermediate':
                if trophic_type[link_to[i]] == 'intermediate':
                    ii += 1
                elif trophic_type[link_to[i]] == 'top':
                    it += 1
        bi = float(bi)/len(link_from)
        bt = float(bt)/len(link_from)
        ii = float(ii)/len(link_from)
        it = float(it)/len(link_from)
        # Take logs - see Murtaugh and Kollath (1997) *** move later
        #bi = log(bi/(1-bi))
        #bt = log(bt/(1-bt))
        #ii = log(ii/(1-ii))
        #it = log(it/(1-it))

        # Attributes: Generality and Vulnerability, the average number of prey
        # eaten per predator and predator per prey respectively
        G = [] # Checked
        V = []
        for i in self:
            member = self[i]
            if member.type == 'species':
                preds = link_from.count(member.id)
                preys = link_to.count(member.id)
                if preds > 0:
                    V.append(preds)
                if preys > 0:
                    G.append(preys)
        G = mean(G)
        V = mean(V)

        # Attributes: n3, n2, n1, n3/n2 n2/n1 Checked
        trophic_level = {} # Checked
        uptolev = []
        for i in trophic_type:
            if trophic_type[i] == 'basal':
                trophic_level[i] = 1
                uptolev.append(i)
        count = 2
        while count <= 3:
            nextlev = []
            for i in uptolev:
                for j in range(0,len(link_from)):
                    if i == link_from[j]:
                        nextlev.append(link_to[j])
            for i in nextlev:
                if trophic_level.has_key(i) == False:
                    trophic_level[i] = count
            uptolev = nextlev
            count += 1
        n3 = trophic_level.values().count(3)
        n2 = trophic_level.values().count(2)
        n1 = trophic_level.values().count(1)
        n3on2 = float(n3)/n2
        n2on1 = float(n2)/n1

        # Attributes: f3 f2 Checked
        f3 = []
        f2 = []
        g3 = []
        g2 = []
        g1 = []
        for id in trophic_level:
            if trophic_level[id] == 3:
                for j in self[id].F:
                    if self[id].F[j] > f_cutoff:
                        f3.append(self[id].F[j])
                        g3.append(self[id].G[j])
            if trophic_level[id] == 2:
                for j in self[id].F:
                    if self[id].F[j] > f_cutoff:
                        f2.append(self[id].F[j])
                        g2.append(self[id].G[j])
            if trophic_level[id] == 1:
                for j in self[id].F:
                    if self[id].F[j] > f_cutoff:
                        g1.append(self[id].G[j])
        f3 = mean(f3)
        f2 = mean(f2)
        g3 = mean(g3)
        g2 = mean(g2)
        g1 = mean(g1)

        return [trophic_level,sz,basal,intermediate,top,bi,bt,ii,it,C,G,V,meanS,n1,n2,n3,n3on2,n2on1,f2,f3,g1,g2,g3]

    # Calculate invasibility 
    def calc_invasibility(self,M,euler_params,params,no_invasions = 200):
        # Speed up calculations
        euler_params['del_t'] = 0.2 # From Drossel
        euler_params['eqm_tol'] = 0.1*euler_params['del_t'] # Doesn't need to be strict for this calc
        euler_params['t_max'] = 10000
        L = 10
        K = len(M)

        count_successes = 0
        # For 100 trials 
        for i in range(0,no_invasions):
            exM = extend_M(M,L) # Extend M by L entries
            web_mod = copy.deepcopy(self)
            # Create the novel invader, which has the new L entries as
            # its traits
            traits = arange(K,K+L) # traits = [50,52,...,59]
            invader_id = max(self.keys()) + 1
            invader = Member(params, id = invader_id, traits = traits)
            # Add to web
            web_mod[invader_id] = invader
            # Equilibriate web
            web_mod.update_S(exM)
            web_mod.update_A(params['c'])
            web_mod.equilibriate(euler_params,params,invader_id)
            # Check if invader survived - increment counter
            if web_mod.has_key(invader_id):
                count_successes += 1

            invasibility = float(count_successes)/no_invasions
            l_invasibility = log(float(count_successes)/(no_invasions-count_successes))
        return [invasibility,l_invasibility]

    # Calculate invasibility old version
    def calc_invasibility_old(self,M,euler_params,params,no_invasions = 100):
        # Speed up calculations
        euler_params['del_t'] = 0.2 # From Drossel
        euler_params['eqm_tol'] = 0.1*euler_params['del_t'] # Doesn't need to be strict for this calc
        euler_params['t_max'] = 10000

        exM = extend_M(M) # Extend M
        count_successes = 0
        # For 100 trials 
        for i in range(0,no_invasions):
            print 'Trialling invader ' + str(i)
            web_mod = copy.deepcopy(self)
            # Create novel_invader
            traits = create_novel_traits(2*params['K'])
            invader_id = max(self.keys()) + 1
            invader = Member(params, id = invader_id, traits = traits)
            # Add to web
            web_mod[invader_id] = invader
            # Equilibriate web
            web_mod.update_S(exM)
            web_mod.update_A(params['c'])
            web_mod.equilibriate(euler_params,params,invader_id)
            # Check if invader survived - increment counter
            if web_mod.has_key(invader_id):
                count_successes += 1

            invasibility = float(count_successes)/no_invasions
            l_invasibility = log(float(count_successes)/(no_invasions-count_successes))
        return [invasibility,l_invasibility]

    # Disturb web by removing up to sz-5 individuals, creating no_sets
    # webs for each size
    def disturb(self,no_sets = 10):
        file_name = 'web1_res1'
        fid = open(file_name + '_dist.pkl', 'wb')
        cPickle.dump('Web created by ***. Pickle file contains disturbed webs',fid)
        sz = len(self)-1
        for x in range(1,sz-4): # For x = 1:sz-5
            for i in range(0,no_sets): 
                web_mod = copy.deepcopy(self)
                # Remove x random species from the web
                rem = web_mod.rand()
                web_mod.remove(rem.id)
            web_mod.equilibriate(euler_params,params) # Equilibriate the web
            cPickle.dump(web_mod,fid) # Output the disturbed web to a file
        fid.close()

        # To read webs
        '''
        fid = open(file_name + '_dist.pkl','rb')
        web = cPickle.load(fid)
        end_file = False
        web_d = {}
        count = 0
        while end_file == False:
            count += 1
            try:
                web_d[count] = cPickle.load(fid)
            except:
                end_file = True
        fid.close()
        '''

    # Evaluate derivative dn_{id_eval}/dt
    def ndot(self,params,id_eval):
        member = self[id_eval]
        if member.type == 'species':
            lam = 0.1 # Parameter from Drossel et al. (2001)
            self.equilibriate_FG(params['b'])
            [gains,losses] = self.gains_losses() # Make more efficient?
            if gains.has_key(id_eval):
                gain = gains[id_eval]
            else:
                gain = 0
            if losses.has_key(id_eval):
                loss = losses[id_eval]
            else:
                loss = 0
            res = -member.n+lam*gain-loss
        else:
            res = 0
        return res

    # Ridder's method
    def ridder(self,params,id_eval,id_pert):
        con = 1.4
        con2 = con*con
        big = 1e30
        ntab = 10
        safe = 2

        a = scipy.zeros((ntab,ntab))
        hh = self[id_pert].n + float(self[id_pert].n)/10
        #hh = h

        pert_web = copy.deepcopy(self)
        pert_web[id_pert].n = pert_web[id_pert].n + hh
        fxphh = pert_web.ndot(params,id_eval)
        pert_web = copy.deepcopy(self)
        pert_web[id_pert].n = pert_web[id_pert].n - hh
        fxmhh = pert_web.ndot(params,id_eval)

        a[0,0] = (fxphh - fxmhh)/(2*hh)
        err = big
        for i in range(1,ntab):
            hh = hh/con

            pert_web = copy.deepcopy(self)
            pert_web[id_pert].n = pert_web[id_pert].n + hh
            fxphh = pert_web.ndot(params,id_eval)
            pert_web = copy.deepcopy(self)
            pert_web[id_pert].n = pert_web[id_pert].n - hh
            fxmhh = pert_web.ndot(params,id_eval)

            a[0,i] = (fxphh - fxmhh)/(2*hh)
            fac = con2
            for j in range(1,i):
                a[j,i] = (a[j-1,i]*fac-a[j-1,i-1])/(fac-1)
                fac = con2*fac
                errt = max(abs(a[j,i]-a[j-1,i]),abs(a[j,i]-a[j-1,i-1]))
                if errt <= err:
                    err = errt
                    res = a[j,i]

            if abs(a[i,i]-a[i-1,i-1]) >= safe*err:
                break

        return res

    # Calculate the Jacobian matrix. Note that you need to
    # equilibriate the web first before sending it here
    # If j_ij is positive, that means i receives a positive effect
    # from j
    def get_J(self,params):
        ids = self.keys()
        sz = len(ids)
        J = scipy.zeros((sz,sz))
        for i in range(0,sz):
            ind_eval = ids[i]
            for j in range(0,sz):
                ind_pert = ids[j]
                J[i,j] = self.ridder(params,ind_eval,ind_pert)
        return [ids,J]

    # Various interaction strength metrics that are calculated from J
    def calc_J_metrics(self,params,ids = None, J = None,trophic_level = None):

        if (ids == None) or (J == None): # Calculate J
            [ids,J] = self.get_J(params)
        
        if trophic_level == None: # Calculate trophic level
            atts = self.get_atts()
            trophic_level = atts.pop(0)

        sz = len(J)
        # All
        meanJ_all = 0
        for i in range(0,sz):
            for j in range(0,sz):
                if abs(J[i,j]) > 0:
                    meanJ_all += abs(J[i,j])
        meanJ_all = meanJ_all/(sz**2)

        # Predation
        meanJ_predn = 0
        count = 0
        # Predation divided by trophic level
        meanJ_3t2 = 0
        meanJ_2t1 = 0
        count_3t2 = 0
        count_2t1 = 0
        for i_id in self:
            member = self[i_id]
            for k_id in member.F:
                J_ik = J[ids.index(i_id),ids.index(k_id)]
                assert J_ik > 0, 'A predation with negative J? (' + str(i_id) + ',' + str(k_id) + ')'
                meanJ_predn += J_ik
                count += 1
                if (trophic_level[i_id] == 3) and (trophic_level[k_id] == 2):
                    meanJ_3t2 += J_ik
                    count_3t2 += 1
                elif (trophic_level[i_id] == 2) and (trophic_level[k_id] == 1):
                    meanJ_2t1 += J_ik
                    count_2t1 += 1
        meanJ_predn = meanJ_predn/count
        meanJ_3t2 = meanJ_3t2/count_3t2
        meanJ_2t1 = meanJ_2t1/count_2t1

        # Inter-specific competition
        meanJ_comp = 0
        count = 0
        for i_id in self:
            member = self[i_id]
            for j_id in member.F:
                for k_id in self:
                    if i_id != k_id:
                        if self[k_id].F.has_key(j_id):
                            # We've found a competitor
                            J_ik = J[ids.index(i_id),ids.index(k_id)]
                            assert J_ik < 0, 'A competition with positive J? (' + str(i_id) + ',' + str(k_id) + ')'
                            meanJ_comp += J_ik
                            count += 1
        meanJ_comp = meanJ_comp/count

        # Intraspecific interaction
        meanJ_self = 0
        for i in range(0,sz):
            meanJ_self += abs(J[i,i])
        meanJ_self = meanJ_self/(sz-1) # Don't count resource

        return [meanJ_all, meanJ_predn, meanJ_3t2, meanJ_2t1, meanJ_comp, meanJ_self]

class Member:

    # Initialise a Member
    def __init__(self, params, prev_id = -1, id = False, traits = [], type = "species"):
        K = params['K']
        R = params['R']
        L = 10 # Same as Drossel et al. (2001)
        lam = 0.1 # Parameter from Drossel et al. (2001)

        if traits == []:
            self.traits = create_traits(K,L)
        else:
            self.traits = traits

        if id == False:
            self.id = prev_id + 1
        else:
            self.id = id

        self.type = type

        self.lineage = {}
        if self.type == 'resource':
            self.n = R/lam
            self.lineage['parent'] = 0
            self.lineage['firstancestor'] = 0
            self.lineage['mutnage'] = 0
        else:
            self.n = 1
            self.lineage['parent'] = self.id
            self.lineage['firstancestor'] = self.id
            self.lineage['mutnage'] = 0

        self.S = {}
        self.A = {}
        self.A[self.id] = 1
        self.F = {}
        self.oldF = {}
        self.G = {}

    def __eq__(self,other):
        if False not in (self.traits == other.traits):
            answer = True
        else:
            answer = False
        return answer

    def calc_a(self,other,c):
        L = 10 # Same as Drossel et al. (2001)

        qsum = 0
        for trait1 in self.traits:
            for trait2 in other.traits:
                if trait1 == trait2:
                    qsum += 1
        q = float(qsum)/L
        return c + (1-c)*q # Equation 12

    # Print Member
    def __repr__(self):
        st = self.type
        st += " "
        st += str(self.id)
        st += ": "
        for trait in self.traits:
            st += str(trait) + " "

        return st
# ------------------------------------
# Main
'''
Examples
========

Reading from Octave output
---------------------------

# Read in Octave-style M matrix
M_file_name = 'novelm2.m'
M = get_M(M_file_name)
K = len(M)

web = get_web('egweb.m',K) # Read in Octave web

Pickling and unpickling webs
----------------------------

fid = open('test.pkl', 'wb')
pickle.dump(web,fid)
fid.close()
fid = open('test.pkl','rb')
poo = pickle.load(fid)
fid.close()


Initialise and do a few steps on a new random web
----------------------------------------------------

# Parameters 
# --------
# Parameters for equilibriating a web
euler_params = {}
euler_params['del_t'] = 0.01 # Time step for Euler method
euler_params['t_max'] = 10000 # Maximum steps of Euler method
euler_params['eqm_tol'] = 0.01*euler_params['del_t'] # From an email from Quince, the tolerance for Euler steady state

# Parameters for building a single web
params = {}
params['R'] = 10000
params['b'] = 0.005
params['c'] = 0.5
params['K'] = 100 # Number of entries in M, made it smaller than in paper


# Parameters for the assembly
inv_max = 20
file_out = 'test.m'

# Create M
M = create_M(K) 


# Initialise web
web = Web() 
web.initialise(params,M) # Now has one resource and one species, at equilibrium
# We've now done max(web.keys()) invasions

# Make a record of number of species
no_mem = [1]
for i in range(1,max(web.keys())):
    no_mem.append(1)
no_mem.append(2)

# Iterate for the rest
for inv in range(max(web.keys())+1,inv_max):
    web.add_offspring(id = inv,K = K)
    web.update_S(M)
    web.update_A(c)
    web.init_F()
    web.equilibriate(euler_params,params)
    no_mem.append(len(web))
    print str(inv) + ': ' + str(len(web))

fid = open('test.pkl', 'wb')
pickle.dump(M,fid)
pickle.dump(web,fid)
pickle.dump(no_mem,fid)
fid.close()


'''
