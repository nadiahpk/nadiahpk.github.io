% make a quiver plot and plot one solution to exponential growth
% dy / dt = lambda y

% parameters
% ---

lambda = 0.3;
t_max = 8;
len_dt = 1;

% plot
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 100, 100]);

% create grid for quiver plot
y_max = t_max; % so it's square
t_range = linspace(0, t_max, 9);
y_range = linspace(0, y_max, 9);
[T, Y] = meshgrid(t_range, y_range);

% compute direction field (dt = 1, dy = lambda * y)
true_dT = len_dt * ones(size(T));
true_dY = len_dt * lambda * Y;

use_tys = [0, 1; 2, 3; 4, 6; 6, 2; 6, 4];
dT = nan(size(T));
dY = nan(size(T));
for i = 1:length(use_tys);
    t = use_tys(i, 1);
    y = use_tys(i, 2);
    t_idx = find(t_range == t);
    y_idx = find(y_range == y);
    dT(y_idx, t_idx) = true_dT(y_idx, t_idx);
    dY(y_idx, t_idx) = true_dY(y_idx, t_idx);
end

% plot quivers
quiver(T, Y, dT, dY, "AutoScale", "off", "Color", [0.9, 0.9, 0.9]); %, 0.5, 'Color', [0.7 0.7 0.7]);

% decorate
title({"solutions to dy/dt = \lambda y", "for \lambda = 0.3"})
xlabel("time t")
ylabel("population size y(t)")
axis equal;

% I want to be able to see the y = 0 arrows
xlim([-1, t_max+1]);
ylim([-1, t_max]);
xticks(0:8);
yticks(0:8);

grid on;
grid minor;

exportgraphics(gcf, 'one_quiver.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')

