def bayes_therom(p_b_given_a,p_a,p_b):
    return (p_b_given_a*p_a)/p_b

#probabilty having disease
p_disease=0.01  #1%
#probability of positive test if disease is present 
p_pos_given_disease=0.99 #(99%)
#probability of positive test if disease is not  present 
p_pos_given_no_disease=0.05 #5%

#overall probabilty of a positive test
p_pos=(
    (p_pos_given_disease)*p_disease + (p_pos_given_no_disease)*(1-(p_disease))
)

#calculation
p_disease_given_pos=bayes_therom(p_pos_given_disease,p_disease,p_pos)
print(f"p(Disease|positive)={p_disease_given_pos:.4f}")
print(f"Means even if test is positive , only{p_disease_given_pos*100:.1f}%chances of disease")