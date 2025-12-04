% make a quiver plot and plot solutions to logistic growth
% dy / dt = lambda * y * (1 - y/K)

% parameters
% ---

lambda = 0.5;
K = 8;  % carrying capacity
t_max = 12;
y_max = 12;

y0s = [2, 12];  % starting with one solution, you can add more

% plot
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 100, 100]);

% plot some solutions
hold on;
t_sol = linspace(0, t_max, 200);
for y0 = y0s
    % analytical solution to logistic equation
    y_sol = K ./ (1 + ((K/y0) - 1) * exp(-lambda * t_sol));
    h = plot(t_sol, y_sol, 'k--', "LineWidth", 1);
    h.Color(4) = 0.1; % make faint
end

% create grid for quiver plot
t_range = linspace(0, t_max, t_max+1);
y_range = linspace(0, y_max, y_max+1);
[T, Y] = meshgrid(t_range, y_range);

% compute direction field (dt = 1, dy = lambda * y * (1 - y/K))
dT = ones(size(T));
dY = lambda * Y .* (1 - Y/K);

% plot quivers
quiver(T, Y, dT, dY, "AutoScale", "on", "Color", "b");
hold off;

% add horizontal line at carrying capacity
% plot([0, t_max], [K, K], 'r:', 'LineWidth', 1);

% decorate
title({"solutions to dy/dt = \lambda y (1 - y/K)", sprintf("for \\lambda = %.1f, K = %d", lambda, K)})
xlabel("time t")
ylabel("population size y(t)")
axis equal;

% set axis limits
xlim([-1, t_max+1]);
ylim([-1, y_max+1]);

exportgraphics(gcf, 'logistic.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')
