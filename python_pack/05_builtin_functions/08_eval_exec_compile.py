"""Use eval and exec only with trusted input."""

expression = "10 + 20 * 2"
print("eval result:", eval(expression))

code = "result = sum([10, 20, 30])"
namespace = {}
exec(code, namespace)
print("exec result:", namespace["result"])

compiled = compile("5 ** 3", "<string>", "eval")
print("compile result:", eval(compiled))
