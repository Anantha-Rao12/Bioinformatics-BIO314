import matplotlib.pyplot as plt
import seaborn as sns

def select_substitution_matrix(integer):
    subs_dict = {1:'blosum62.csv',2:'blosum50.csv',3:'pam100.csv',4:'pam250.csv'}
    if integer in subs_dict:
        return subs_dict[integer]
    else:
        print('Input error!')

def conv_list2str(list_obj) :
    """ Helper function to obtain alignment sequence """

    string = ''
    return string.join(list_obj)


def plot_align_matrix(M,seq1,seq2,Global):

    """ Plot the Global Alignment scores matrix """

    fig = plt.figure(figsize=(30,26),dpi=65)
    ax = fig.add_axes([0.1,0.1,0.8,0.8])

    sns.heatmap(M,linewidth=0.9,ax=ax,annot=True,cmap='magma',fmt='.3g')
    if Global == True:
        ax.set_title('Global Alignment Score Matrix')
    else : 
        ax.set_title('Local Alignment Score Matrix')
 
    ax.set_xticklabels(['Gap']+[letter for letter in seq2],fontsize=10)
    ax.set_xlabel('Sequence 2',fontsize=16)
    ax.xaxis.tick_top()

    ax.set_yticklabels(['Gap']+[letter for letter in seq1],fontsize=10, rotation=45)
    ax.set_ylabel('Sequence 1',fontsize=16)

    return ax 

def plot_tracer(T,seq1,seq2,Global):

    """ Plot the traceback route """

    fig = plt.figure(figsize=(30,26))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])

    sns.heatmap(T,linewidth=0.9,ax=ax, cmap='coolwarm',cbar=False)
    if Global == True:
        ax.set_title('Global Alignment Traceback')
    else : 
        ax.set_title('Local Alignment Traceback')
    ax.set_xticklabels(['Gap']+[letter for letter in seq2],fontsize=10)
    ax.set_xlabel('Sequence 2',fontsize=16)
    ax.xaxis.tick_top()
    ax.set_yticklabels(['Gap']+[letter for letter in seq1],fontsize=10, rotation=45)
    ax.set_ylabel('Sequence 1',fontsize=16)

    return ax

