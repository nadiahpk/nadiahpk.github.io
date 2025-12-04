% make a quiver plot and plot solutions to logistic growth
% dy / dt = lambda * y * (1 - y/K)

clear;

% parameters
% ---

% critical h values are h = 0 (when flat, oscillation starts) and h = 4 (oscillation diverges
h = 3.5;
fout_name = 'logistic_euler_osc_stable.pdf';

h = 1;
fout_name = 'logistic_euler_stable.pdf';

h = 4.5;
fout_name = 'logistic_euler_unstable.pdf';

% fixed parameters
lambda = 0.5;
K = 8;  % carrying capacity
t_max = 40;
y_max = 10;  % compact

y0 = 1; %K; % just one solution

% arrow scaling
dt = 1;

% function
dydt = @(y) y * lambda * (1 - y / K);

% euler's method with large step size
% ---

nbr_steps = floor(t_max / h);
yV = zeros(nbr_steps+1, 1);
yV(1, 1) = y0;
tV = (0:h:t_max)';
for i = 1:nbr_steps
    yV(i+1) = yV(i) + h * dydt(yV(i));
end



% plot
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 200, 80]);

% plot Euler steps
plot_properties = plot(tV, yV, 'k-', "LineWidth", 1);
plot_properties.Color(4) = 0.1; % make faint
hold on;
scatter(tV, yV, 'o', "MarkerEdgeColor", [0.9, 0.9, 0.9]);

% plot true solution
t_sol = linspace(0, t_max, 200);
y_sol = K ./ (1 + ((K/y0) - 1) * exp(-lambda * t_sol));
plot(t_sol, y_sol, 'r-', "LineWidth", 1);

% create grid for quiver plot
% t_range = linspace(0, t_max, y_max+1);
t_range = 0:dt:t_max;
y_range = linspace(0, y_max, y_max+1);
[T, Y] = meshgrid(t_range, y_range);

% compute direction field (dt = 1, dy = lambda * y * (1 - y/K))
dT = dt * ones(size(T));
dY = dt * lambda * Y .* (1 - Y/K);

% plot quivers
quiver(T, Y, dT, dY, "AutoScale", "on", "Color", [0.2, 0.2, 1]);
hold off;

% add horizontal line at carrying capacity
% plot([0, t_max], [K, K], 'r:', 'LineWidth', 1);

% decorate
% title({"solutions to dy/dt = \lambda y (1 - y/K)", sprintf("for \\lambda = %.1f, K = %d", lambda, K)})
xlabel("time t")
ylabel("population size y(t)")
%axis equal;

% set axis limits
xlim([0, t_max]);
ylim([0, y_max]);
xticks([0:h:t_max]);

exportgraphics(gcf, fout_name, 'ContentType', 'vector', 'BackgroundColor', 'none')
