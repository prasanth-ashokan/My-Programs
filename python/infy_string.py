def sp(a):
    al=len(a);sw=al//3;swl=[];ra=len(a)%3
    for i in range(0,al,sw):
        sws=(a[i:i+sw]);swl.append(sws)
    if ra%3==0:
        return swl
    elif ra%3==2:
        aa=[];aa.append(swl[0]+swl[1]);aa.append(swl[2]);aa.append(swl[3]+swl[4])
        return (aa)
    else:
        aaa=[];aaa.append(swl[0]);aaa.append(swl[1]+swl[2]);aaa.append(swl[3])
        return aaa
a=[i for i in "John"];b=[i for i in "Johny"];c=[i for i in "Janardhan"]
aa=sp(a);bb=sp(b);cc=sp(c)
tl1=[];tl1.append(aa[0]);tl1.append(bb[1]);tl1.append(cc[2])
tl2=[];tl2.append(aa[1]);tl2.append(bb[2]);tl2.append(cc[0])
tl3=[];tl3.append(aa[2]);tl3.append(bb[0]);tl3.append(cc[1])

    
