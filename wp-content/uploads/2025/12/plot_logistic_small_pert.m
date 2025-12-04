% make a quiver plot and plot solutions to logistic growth
% dy / dt = lambda * y * (1 - y/K)

clear;

% parameters
% ---

% critical h values are h = 0 (when flat, oscillation starts) and h = 4 (oscillation diverges
h = 4.5;
fout_name = 'logistic_small_pert.pdf';

% fixed parameters
lambda = 0.5;
K = 8;  % carrying capacity
t_max = 40;
y_max = 10;  % compact

y0 = K+0.1; %K; % just one solution

% arrow scaling
dt = 1;

% shift t so we're continuing
shift_t = 50;

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
plot_properties = plot(tV+shift_t, yV, 'k-', "LineWidth", 1);
plot_properties.Color(4) = 0.1; % make faint
hold on;
scatter(tV+shift_t, yV, 'o', "MarkerEdgeColor", [0.9, 0.9, 0.9]);

% create grid for quiver plot
% t_range = linspace(0, t_max, y_max+1);
t_range = shift_t:dt:shift_t+t_max;
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
xlim([shift_t, shift_t+t_max]);
ylim([0, y_max]);
xticks(shift_t+tV);

exportgraphics(gcf, fout_name, 'ContentType', 'vector', 'BackgroundColor', 'none')
