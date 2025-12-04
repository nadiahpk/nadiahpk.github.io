% make a dy/dt vs y plot that shows steady states

clear;

% parameters
% ---

lambda = 0.3;
y_max = 10;

% plot dy/dt vs y
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 100, 80]);

% plot relationship
y_range = linspace(0, y_max, 11);
dydt = lambda .* y_range;
h = plot(y_range, dydt, "k--", "LineWidth", 1);
h.Color(4) = 0.1; % make faint

% line for y = 0
yline(0, "k", "LineWidth", 1);

% decorate
title("y versus dy/dt = 0.3 y")
xlabel("population size y")
ylabel("change in population size dy/dt")

% I want to be able to see the y = 0 arrows
xlim([-0.9, y_max]);
ylim([-0.9, max(dydt) + 0.5]);
yticks(0:max(dydt)+0.5);

exportgraphics(gcf, 'expon_growth_dydt.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')

