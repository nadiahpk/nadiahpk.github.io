% make a quiver plot and plot one solution to exponential growth
% dy / dt = lambda y

% parameters
% ---

lambda = 0.3;
t_max = 10;
y_max = 12;

y0 = 1;
h = 5; % step size

% plot
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 100, 100]);

% plot one solution
t_sol = linspace(0, t_max, 100);
y_sol = y0 * exp(lambda * t_sol);
plot(t_sol, y_sol, 'r-', "LineWidth", 1);
hold on;

% create grid for quiver plot
t_range = linspace(0, t_max, 11);
y_range = linspace(0, y_max, y_max + 1);
[T, Y] = meshgrid(t_range, y_range);

% compute direction field (dt = 1, dy = lambda * y)
dT = ones(size(T));
dY = lambda * Y;

% plot quivers
quiver(T, Y, dT, dY, "AutoScale", "on", "Color", [0.3, 0.3, 1]); %, 0.5, 'Color', [0.7 0.7 0.7]);

% do two Euler steps
tV = [0, h, 2*h];
y1 = y0 + h * lambda * y0;
y2 = y1 + h * lambda * y1;
line_prop = plot(tV, [y0, y1, y2], 'k--', "LineWidth", 1);
line_prop.Color(4) = 0.1; % make faint

% decorate
% title({"solutions to dy/dt = \lambda y", "for \lambda = 0.3"})
xlabel("time t")
ylabel("population size y(t)")
axis equal;
%xticks([0:t_max]);
grid on;
grid minor;

% I want to be able to see the y = 0 arrows
xlim([-1, t_max+1]);
ylim([-1, y_max+1]);

hold off;
exportgraphics(gcf, 'expon_growth_euler.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')

