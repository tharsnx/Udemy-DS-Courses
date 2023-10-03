t.figure(figsize=(15,40))
    t = {'Average': average_rate,'Max' : max_rate}
    tf = pd.DataFrame(t,columns=['Average','Max'],index=name_instr)
    tf.plot.bar()
    plt.savefig('hello world.png')
    plt.show()