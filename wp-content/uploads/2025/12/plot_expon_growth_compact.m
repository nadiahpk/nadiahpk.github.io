% make a quiver plot and plot one solution to exponential growth
% dy / dt = lambda y

% parameters
% ---

lambda = 0.3;
t_max = 10;

y0s = [0, 1, 2, 4];

% plot
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 100, 100]);

% plot some solutions
hold on;
t_sol = linspace(0, t_max, 100);
for y0 = y0s
    y_sol = y0 * exp(lambda * t_sol);
    h = plot(t_sol, y_sol, 'r-', "LineWidth", 2);
    % h.Color(4) = 0.1; % make faint
end

% create grid for quiver plot
y_max = t_max-1; % compact
t_range = linspace(0, t_max, 11);
y_range = linspace(0, y_max, y_max + 1);
[T, Y] = meshgrid(t_range, y_range);

% compute direction field (dt = 1, dy = lambda * y)
dT = ones(size(T));
dY = lambda * Y;

% plot quivers
quiver(T, Y, dT, dY, "AutoScale", "on", "Color", [0.2, 0.2, 1]); %, 0.5, 'Color', [0.7 0.7 0.7]);
hold off;

% decorate
% title({"solutions to dy/dt = \lambda y", "for \lambda = 0.3"})
xlabel("time t")
ylabel("population size y(t)")
axis equal;

% I want to be able to see the y = 0 arrows
xlim([-1, t_max+1]);
ylim([-1, t_max-1]);

exportgraphics(gcf, 'expon_growth_compact.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')

