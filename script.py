import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

#fetchmaker.get_weight("poodle")
#fetchmaker.get_tail_length("poodle")
#fetchmaker.get_age("poodle")
#fetchmaker.get_color("brown","grey")
#fetchmaker.get_is_rescue(0,1)

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print (np.mean(rottweiler_tl))
print (np.std(rottweiler_tl))

whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
print binom_test(num_whippet_rescues, num_whippets, 0.08)

"""Three of our most popular mid-sized dog breeds are whippets, terriers, and pitbulls. Is there a significant difference in the average weights of these three dog breeds? Perform a comparative numerical test to determine if there is a significant difference."""
w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")
print f_oneway(w, t, p).pvalue

"""Now, perform another test to determine which of the pairs of these dog breeds differ from each other."""
values = np.concatenate([w, t, p])
labels = ['whippet'] * len(w) + ['terrier'] * len(t) + ['pitbull'] * len(p)

print pairwise_tukeyhsd(values, labels, .05)


poodle_colors = fetchmaker.get_color("poodle")
shihtzu_color = fetchmaker.get_color("shihtzu")
color_table = [
  [np.count_nonzero(poodle_colors == "black"), 
  np.count_nonzero(shihtzu_color == "black")],
   [np.count_nonzero(poodle_colors == "brown"), 
  np.count_nonzero(shihtzu_color == "brown")],
   [np.count_nonzero(poodle_colors == "gold"), 
  np.count_nonzero(shihtzu_color == "gold")],
  [np.count_nonzero(poodle_colors == "grey"), 
  np.count_nonzero(shihtzu_color == "grey")],
   [np.count_nonzero(poodle_colors == "white"), 
  np.count_nonzero(shihtzu_color == "white")],
]
print color_table

chi2, color_pval, dof, expected = chi2_contingency(color_table)
print color_pval


