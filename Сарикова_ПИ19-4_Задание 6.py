from scipy.optimize import linprog

# Вариант 40
#F(x1, x2,x3) = 36x1 + 42x2+32x3 → max
#x1 + 3x2+4x3<= 3000,
#6x1 + 5x2+2x4<= 3320,
#x1,x2,x3 >=0.

# Берем из первой строки коэффициенты, если будет x4, то добавляем в список еще значение и так далее
obj = [-36, -42, -32]

# Берем коэффициенты из неравенств, если переменная пропущена, то 0
lhs_ineq = [[1, 3, 4],  # неравенство 1
            [6, 5, 2]]  # неравенство 2

# Берем значения, которое больше неравенств
rhs_ineq = [ 3000,  # Рабочая сила
            3320]  # Материал B

# решаем
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")

#print(opt) наша переменная
print(f'Ответ. X∗ = ({opt.x[0]}; {opt.x[1]}; {opt.x[2]}); Fmax = F(X∗) = {opt.fun}')