import replicate


queryMsg ="what is your name?"

input = {
    "prompt": queryMsg,
    "temperature": 1
}

output = replicate.run(
    "joehoover/falcon-40b-instruct:7d58d6bddc53c23fa451c403b2b5373b1e0fa094e4e0d1b98c3d02931aa07173",
    input=input
)
print("".join(output))
#=> "Thy heart shall bloom like an open source flower,\nAnd l...