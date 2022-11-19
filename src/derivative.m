syms x r
f = x .^ r

g = diff(f)
% ans = r * x .^ (r-1)

subs(g, [x, r], [3, 2])
% ans = 6
