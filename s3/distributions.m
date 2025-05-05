% Summary: Beta distribution skews to low numbers
% (betadistribution.eps), so it spreads out
% the number of prey each predator has, so that even those very high
% in trophic level can also have just a few prey (see
% comparing_no_prey_orig_and_generalised_cascade.eps)

% The purpose of this script is to plot the distributions of ri for
% the Cascade Model and the Generalised Cascade Model (from Stouffer)
% to try and figure out what the significance of the exponential
% function is
%
% In the original Cascade Model, species j with nj < ni becomes a prey 
% of i with fixed probability x0 = 2CS/(S - 1)
%
% In the Generalised Cascade Model, species i preys on
% species j with nj < ni, with a species-specific probability
% x drawn—from the beta distribution or an exponential
% distribution—from the interval [0, 1]
%
% So what we should see a difference in is the number of prey versus
% ni
%
% The Beta Distribution describes a distribution of x, 0 < x < 1,
% where the probability of a particular value for x is given by:
%
% p(x) = \beta(1-x)^{\beta-1} 
%
% If y is a uniform random variable, you can generate x with a Beta
% Distribution using:
%
% x = 1-(1-y)^(1/beta)
%
% The Beta Distribution has the expected value E(x) = 1/(1+beta), so
% Beta can also be selected to satisfy the connectance criteria c, so
%
% beta = 1/(2*c) - 1;
%

% Let's use Little Rock Lake, which has 92 species and a connectance of 0.12
S = 92;
C = 0.12;
beta = 1/(2*C) - 1;

n = rand(S,1); % random niche value

% Niche Model
y = rand(S,1);
x = (1-(1-y).^(1/beta)); 
r = n.*x;
c = rand*(n-r/2)+r/2;

niche_no_prey = zeros(S,1);
for i = 1:S
    ci = c(i);
    ri = r(i);
    low_bound = ci-ri/2;
    upp_bound = ci+ri/2;
    niche_no_prey(i) = length(find((n > low_bound) & (n < upp_bound)));
end

% Cascade Models:
potl_prey_V = zeros(S,1);
for i = 1:S
    potl_prey_V(i) = length(find(n<n(i)));
end
% In the original Cascade Model, species j with nj < ni becomes a prey 
% of i with fixed probability x0 = 2CS/(S - 1)
cascade_x = 2*C*S/(S-1);
cascade_no_prey = zeros(S,1);
% about cascade_x * potl_no_prey
for i = 1:S
    potl_prey = find(n<n(i));
    for j = 1:length(potl_prey)
        if rand > cascade_x
            cascade_no_prey(i) += 1;
        end
    end
end

% In the Generalised Cascade Model, species i preys on
% species j with nj < ni, with a species-specific probability
% x drawn—from the beta distribution or an exponential
% distribution—from the interval [0, 1]
gen_cascade_no_prey = zeros(S,1);
for i = 1:S
    potl_prey = find(n<n(i));
    predator_specific_x = (1-(1-rand).^(1/beta)); 
    for j = 1:length(potl_prey)
        if rand > predator_specific_x
            gen_cascade_no_prey(i) += 1;
        end
    end
end

hold off
plot(n,potl_prey_V,';maximum possible;ko')
hold on
plot(n,cascade_no_prey,';original cascade;bx')
plot(n,gen_cascade_no_prey,';generalised cascade;rx')
%plot(n,niche_no_prey,';niche;kx')
legend ({"maximum possible", "original cascade","generalised cascade"}, "location", "northwest")
hold off
