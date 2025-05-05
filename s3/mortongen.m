% An example of checking permanence and measuring the distance from
% the convex hull to the set D

% Define Lotka-Volterra coefficients
A = [
-.00061 -.000207 -.052365 -.001789
-.00040 -.000139 -.001260 -.064501
0.00574 0.000033 0        -.096816
0.00001 0.000151 0.000399 0
];
r = [.220737 .164163 -.087756 -.096189]';

nospp = length(r);

% Identify all subsystems and put in subStore
subStore = zeros(1,nospp-1);
for cnt = 1:nospp
	subStore = [subStore;[cnt,zeros(1,nospp-2)]];
end
for sublngth = 2:nospp - 1;
	% Get all subsystems of length sublngth
	subMat = 1:sublngth;
	termsub = subMat + (nospp-sublngth);
	subMat = recurseplanes(subMat,termsub);
	% Now append to subStore
	lengthSubMat = size(subMat,1);
	subMat = [subMat,zeros(lengthSubMat,nospp-sublngth-1)];
	subStore = [subStore;subMat];
end
noSubs = size(subStore,1);

% Now find subsystems' steady states, and identify those that are positive
posSubs = 1; % Store a list of positive subsystems
xStore = zeros(1,nospp); % Store the boundary equilibria
for subCnt = 2:noSubs;
	% Acquire list of species absent and present
	present = subStore(subCnt,:);
	present(find(present == 0)) = [];
	absent = 1:nospp; absent(present) = [];

	% Evaluate boundary equilibrium
	ANow = A;
	ANow(absent,:) = []; ANow(:,absent) = [];
	rNow = r; rNow(absent) = [];
	if rank(ANow) == size(ANow,1);
		xSub = ANow\-rNow;

		% Put into a single vector steady states of those absent and
		% present
		xNow = zeros(nospp,1);
		cntPresent = 1;
		for cntPresent = 1:length(present);
			xNow(present(cntPresent)) = xSub(cntPresent);
		end

		% If positive, make a note of it
		if min(xNow) >= 0
			posSubs = [posSubs; subCnt];
		end

		% Record steady state
		xStore = [xStore;xNow'];
	else
		% Record as zeros
		xStore = [xStore;zeros(1,nospp)];
	end
end

% For each positive subsystem, calculate the transversal eigenvalue
lengthPos = size(posSubs,1);
% Store eigenvalues in G, rows correspond to subsystem and columns to species
G = []; 
for posSubCnt = 1:lengthPos
	subCnt = posSubs(posSubCnt,1);
	rowofG = A*(xStore(subCnt,:)')+r;
	% Get rid of small values
	present = subStore(subCnt,:);
	present(find(present==0)) = [];
	absent = 1:nospp; absent(present) = [];
	rowofG(present) = 0;
	G = [G;rowofG'];
end

% The linear programming problem, for verifying permanence
G = [G,ones(lengthPos,1)]; % [G,ones]
c = zeros(nospp+1,1); c(nospp+1) = 1;
b = zeros(lengthPos,1);

ctypestr = [];
for cnt = 1:lengthPos
	ctypestr = [ctypestr,"L"];
end
vartypestr = [];
for cnt = 1:nospp+1
	vartypestr = [vartypestr,"C"];
end

[p,zmin] = glpk(c,G,b,[zeros(nospp,1);-Inf],[ones(nospp,1);0],ctypestr,vartypestr);

p = p(1:nospp); % The vector that defines the Lyapunov fnc

disp('p = ')
disp('p')
disp('zmin = ')
disp(zmin);

if (zmin < 0) & min(p(1:nospp)>0)
	disp('the system is permanent')
else
	disp('the system is not permanent')
end

% Find Hofbauer & Sigmund's separating functional n
n = (p'*A)';

if min(n) < 0
	n = n./min(n)
else
	n = n./max(n)
end

xs = A\-r; % Steady state of the whole system
nospp = length(xs);
tol = 1e-10; % For rounding error

% calculated distances from hyperplanes passing through each boundary
% equilibria to the interior equilibrium xs
d = (n'*xs-xStore(posSubs,:)*n)/norm(n);
disp('d = ')
disp(d)
mind = min(d);
disp('smallest distance = ')
disp(mind)
