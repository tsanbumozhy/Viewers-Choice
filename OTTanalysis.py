# Python program to perform OTT graph analysis using provided data with tkinter, pandas and matplotlib libraries

import tkinter.ttk
from tkinter import *
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# creating tkinter window
root = Tk()
root.configure(bg = 'black')
root.attributes('-fullscreen', True)

# Creating a photoimage object to use image
Netflixlogo= PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\Netflix.png")
netflixgraphimage = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\netflixgraph.png")
Primelogo = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\Prime.png")
primegraphimage = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\primegraph.png")
Hululogo = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\Hulu.png")
hulugraphimage = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\hulugraph.png")
Hotstarlogo = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\Hotstar.png")
hotstargraphimage = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\hotstargraph.png")
comparelogo = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\compare.png")

exitimage = PhotoImage(file=r"C:\Users\potte\Documents\Mini_project_sem-2\Python\images\exit.png")

def Netflix():
    netflixwindow = Toplevel(root)
    netflixwindow.configure(bg='#1C1C1C')
    netflixwindow.title("Netflix")
    netflixwindow.geometry("1250x500")

    title = Label(netflixwindow, text= 'Netflix', font =('Bebas Neue', 24))
    title.configure(fg='#E50914', bg='#1C1C1C')
    title.place(relx=0.05, rely=0.05)

    netflixdescription = '''    Netflix is an American subscription streaming service and production company.
    Launched on August 29, 1997, it offers a film and TV series library through 
    distribution deals as well as its own productions, known as Netflix Originals.'''

    Textwindow = Text(netflixwindow, height=5.5, width=80)

    Textwindow.place(relx=0.075, rely=0.17)
    Textwindow.insert('end', netflixdescription)
    Textwindow.configure(state='disabled', font=('Bebas Neue',16), fg='white', bg='#1C1C1C', bd=0)

    def netflixwiki():
        webbrowser.open("https://en.wikipedia.org/wiki/Netflix")

    learnmore = tkinter.Button(Textwindow, text="Learn More", font =('Bebas Neue', 12), command=netflixwiki)
    learnmore.place(relx=0.35, rely=0.6)

    def netfliximage():
        webbrowser.open("https://about.netflix.com/en")

    logoinfo = tkinter.Button(netflixwindow, command=netfliximage, image=Netflixlogo, bd=0, bg='black')
    logoinfo.place(relx=0.7, rely=0.1)


    def netflixgraph():
        netflixgwindow = Toplevel(netflixwindow)
        netflixgwindow.configure(bg='white')
        netflixgwindow.title("Netflix_Graphs")
        netflixgwindow.geometry("1500x700")

        netflixstats = pd.read_csv(r"C:\Users\potte\Documents\Mini_project_sem-2\Python\datasets\netflix_titles.csv")
        netflixstats = netflixstats.sort_values(by=["release_year"], ascending=False)

        type = list(netflixstats["type"])
        listed_in = list(netflixstats["listed_in"])
        country = list(netflixstats["country"])
        release_year = list(netflixstats["release_year"])

        genre = ['Comedy','Action','Horror','Anime','Family','Drama', 'Docu']

        genremcount = []
        for x in range(1, 8):
            genremcount.append(0)

        for x in listed_in:
            if 'Comedies' in str(x):
                genremcount[0] += 1
            if "Action & Adventure" in str(x):
                genremcount[1] += 1
            if "Horror" in str(x):
                genremcount[2] += 1
            if "Anime" in str(x):
                genremcount[3] += 1
            if "Family" in str(x):
                genremcount[4] += 1
            if "Dramas" in str(x):
                genremcount[5] += 1
            if "Documentaries" in str(x):
                genremcount[6] += 1

        eras = []
        eracount = []
        for x in range(1, 8):
            eracount.append(0)

        for x in range(1960, 2030, 10):
            eras.append(str(x) + "'s")

        for x in release_year:
            if x < 2000:
                if x in range(1960, 1970):
                    eracount[0] += 1
                elif x in range(1970, 1980):
                    eracount[1] += 1
                elif x in range(1980, 1990):
                    eracount[2] += 1
                else:
                    eracount[3] += 1
            else:
                if x in range(2000, 2010):
                    eracount[4] += 1
                elif x in range(2010, 2020):
                    eracount[5] += 1
                else:
                    eracount[6] += 1

        origin = ['Japan', 'U.S.', 'Canada', 'India', 'U.K.', 's.Korea', 'France', 'Egypt']
        originmcount = []
        for x in range(1, 9):
            originmcount.append(0)

        for x in country:
            if "Japan" in str(x):
                originmcount[0] += 1
            elif "United States" in str(x):
                originmcount[1] += 1
            elif "Canada" in str(x):
                originmcount[2] += 1
            elif "India" in str(x):
                originmcount[3] += 1
            elif "United Kingdom" in str(x):
                originmcount[4] += 1
            elif "South Korea" in str(x):
                originmcount[5] += 1
            elif "France" in str(x):
                originmcount[6] += 1
            elif "Egypt" in str(x):
                originmcount[7] += 1

        data1 = {"Genre": genre, "Movie Count": genremcount}
        df1 = pd.DataFrame(data1, columns=['Genre', 'Movie Count'])

        data3 = {"Year": eras, "Movie count": eracount}
        df3 = pd.DataFrame(data3, columns=['Year', 'Movie count'])

        figure1 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, netflixgwindow)
        line1.get_tk_widget().grid(row=2, column=1, columnspan=5, rowspan=6)
        df1 = df1[['Genre', 'Movie Count']].groupby('Genre').sum()
        df1.plot(kind='line', ax=ax1, color='#b32222', marker='o', fontsize=10)
        ax1.set_title('Different Genres of movies on Netflix')

        figure2 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax2 = figure2.add_subplot(111)
        colors = ['#99ff99','#fc4c42','#66b3ff','#ffcc99','#ff9999','#c2c2f0','#effd5f','#bf9bde']
        explode = [0, 0.05, 0, 0, 0, 0, 0, 0]
        ax2.pie(originmcount, autopct=lambda pct: "{:1.1f}%".format(pct), colors=colors,explode=explode, shadow=True)
        ax2.legend(origin)
        pie2 = FigureCanvasTkAgg(figure2, netflixgwindow)
        pie2.get_tk_widget().grid(row=2, column=10, columnspan=5, rowspan=6)
        pie2.draw()
        ax2.set_title('Movies on Netflix from different countries')

        figure3 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax3 = figure3.add_subplot(111)
        bar3 = FigureCanvasTkAgg(figure3, netflixgwindow)
        bar3.get_tk_widget().grid(row=2, column=20, columnspan=5, rowspan=6)
        df3 = df3[['Year', 'Movie count']].groupby('Year').sum()
        df3.plot(kind='bar', color= '#0291bc', legend=True, ax=ax3)
        ax3.set_title('Movies on Netflix from different eras')

        flixmoviecount = 0
        flixshowcount = 0

        for x in type:
            if x== "Movie":
                flixmoviecount += 1
            else:
                flixshowcount += 1

        def dispmcount():
            mcount['text'] = "Number of movies in Netflix : " + str(flixmoviecount)
            mcount['fg'] = '#E50914'

        def disptvcount():
            tvcount['text'] = "Number of TV shows in Netflix : " + str(flixshowcount)
            tvcount['fg'] = '#E50914'

        mcount = tkinter.Button(netflixgwindow, text ='Click to display number of movies in Netflix', command=dispmcount, font=('Bebas Neue',16))
        mcount.configure(fg='black')
        mcount.place(relx=0.36, rely=0.75)
        tvcount = tkinter.Button(netflixgwindow, text='Click to display number of TV shows in Netflix', command=disptvcount, font=('Bebas Neue', 16))
        tvcount.configure(fg='black')
        tvcount.place(relx=0.35, rely=0.8)


    generategraph = tkinter.Button(netflixwindow, image=netflixgraphimage, command=netflixgraph)
    generategraph.place(relx=0.32, rely=0.65)

def Prime():
    primewindow = Toplevel(root)
    primewindow.configure(bg='#1C1C1C')
    primewindow.title("Prime")
    primewindow.geometry("1250x500")

    title = Label(primewindow, text= 'Prime Video', font =('Bebas Neue', 24))
    title.configure(fg='#00A8E1', bg='#1C1C1C')
    title.place(relx=0.05, rely=0.05)

    primedescription = '''    Amazon Prime Video is an American subscription video on-demand over-the-top 
    streaming and rental service of Amazon offered as a standalone service or 
    as part of Amazon's Prime subscription. The service primarily distributes films 
    and television series produced by Amazon Studios or licensed to Amazon, 
    as Amazon Originals, with the service also hosting content from other providers,
    content add-ons, live sporting events, and video rental and purchasing services.'''

    Textwindow = Text(primewindow, height=10, width=80)

    Textwindow.place(relx=0.075, rely=0.17)
    Textwindow.insert('end', primedescription)
    Textwindow.configure(state='disabled', font=('Bebas Neue',16), fg='white', bg='#1C1C1C', bd=0)

    def primewiki():
        webbrowser.open("https://en.wikipedia.org/wiki/Amazon_Prime_Video")

    learnmore = tkinter.Button(Textwindow, text="Learn More", font =('Bebas Neue', 12), command=primewiki)
    #learnmore.configure(fg='#E50914',bg='#1C1C1C')
    learnmore.place(relx=0.35, rely=0.65)

    def primeimage():
        webbrowser.open("https://www.primevideo.com/")

    logoinfo = tkinter.Button(primewindow, command=primeimage, image=Primelogo, bd=0, bg='black')
    logoinfo.place(relx=0.7, rely=0.1)


    def primegraph():
        primegwindow = Toplevel(primewindow)
        primegwindow.configure(bg='white')
        primegwindow.title("Prime_Graphs")
        primegwindow.geometry("1500x700")

        primestats = pd.read_csv(r"C:\Users\potte\Documents\Mini_project_sem-2\Python\datasets\amazon_prime_titles.csv")
        primestats = primestats.sort_values(by=["release_year"], ascending=False)

        type = list(primestats["type"])
        listed_in = list(primestats["listed_in"])
        country = list(primestats["country"])
        release_year = list(primestats["release_year"])

        genre = ['Comedy','Action','Horror','Romance','Family','Drama', 'Docu']

        genremcount = []
        for x in range(1, 8):
            genremcount.append(0)

        for x in listed_in:
            if "Comedy" in str(x):
                genremcount[0] += 1
            if "Action" in str(x):
                genremcount[1] += 1
            if "Horror" in str(x):
                genremcount[2] += 1
            if "Romance" in str(x) or "Entertainment" in str(x):
                genremcount[3] += 1
            if "Kids" in str(x):
                genremcount[4] += 1
            if "Drama" in str(x):
                genremcount[5] += 1
            if "Documentary" in str(x):
                genremcount[6] += 1

        eras = []
        eracount = []
        for x in range(1, 8):
            eracount.append(0)

        for x in range(1960, 2030, 10):
            eras.append(str(x) + "'s")

        for x in release_year:
            if x < 2000:
                if x in range(1960, 1970):
                    eracount[0] += 1
                elif x in range(1970, 1980):
                    eracount[1] += 1
                elif x in range(1980, 1990):
                    eracount[2] += 1
                else:
                    eracount[3] += 1
            else:
                if x in range(2000, 2010):
                    eracount[4] += 1
                elif x in range(2010, 2020):
                    eracount[5] += 1
                else:
                    eracount[6] += 1

        origin = ['Australia', 'U.S.', 'Canada', 'India', 'U.K.', 'Others']
        originmcount = []
        for x in range(1, 7):
            originmcount.append(0)

        for x in country:
            if "Australia" in str(x):
                originmcount[0] += 1
            elif "United States" in str(x):
                originmcount[1] += 1
            elif "Canada" in str(x):
                originmcount[2] += 1
            elif "India" in str(x):
                originmcount[3] += 1
            elif "United Kingdom" in str(x):
                originmcount[4] += 1
            elif "France" in str(x) or "Spain" in str(x) or "Italy" in str(x):
                originmcount[5] += 1

        data1 = {"Genre": genre, "Movie Count": genremcount}
        df1 = pd.DataFrame(data1, columns=['Genre', 'Movie Count'])

        data3 = {"Year": eras, "Movie count": eracount}
        df3 = pd.DataFrame(data3, columns=['Year', 'Movie count'])

        figure1 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, primegwindow)
        line1.get_tk_widget().grid(row=2, column=1, columnspan=5, rowspan=6)
        df1 = df1[['Genre', 'Movie Count']].groupby('Genre').sum()
        df1.plot(kind='line', ax=ax1, color='#b32222', marker='o', fontsize=10)
        ax1.set_title('Different Genres of movies on prime')

        figure2 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax2 = figure2.add_subplot(111)
        colors = ['#66b3ff', '#99ff99', '#bf9bde', '#ffcc99', '#ff9999', '#effd5f']
        explode = [0, 0.05, 0, 0, 0, 0]
        ax2.pie(originmcount, autopct=lambda pct: "{:1.1f}%".format(pct), colors=colors,explode=explode, shadow=True)
        ax2.legend(origin)
        pie2 = FigureCanvasTkAgg(figure2, primegwindow)
        pie2.get_tk_widget().grid(row=2, column=10, columnspan=5, rowspan=6)
        pie2.draw()
        ax2.set_title('Movies on prime from different countries')

        figure3 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax3 = figure3.add_subplot(111)
        bar3 = FigureCanvasTkAgg(figure3, primegwindow)
        bar3.get_tk_widget().grid(row=2, column=20, columnspan=5, rowspan=6)
        df3 = df3[['Year', 'Movie count']].groupby('Year').sum()
        df3.plot(kind='bar', color= '#0291bc', legend=True, ax=ax3)
        ax3.set_title('Movies on prime from different eras')

        primmoviecount = 0
        primshowcount = 0

        for x in type:
            if x== "Movie":
                primmoviecount += 1
            else:
                primshowcount += 1

        def dispmcount():
            mcount['text'] = "Number of movies in prime : " + str(primmoviecount)
            mcount['fg'] = '#00A8E1'

        def disptvcount():
            tvcount['text'] = "Number of TV shows in prime : " + str(primshowcount)
            tvcount['fg'] = '#00A8E1'

        mcount = tkinter.Button(primegwindow, text ='Click to display number of movies in prime', command=dispmcount, font=('Bebas Neue',16))
        mcount.configure(fg='black')
        mcount.place(relx=0.36, rely=0.75)
        tvcount = tkinter.Button(primegwindow, text='Click to display number of TV shows in prime', command=disptvcount, font=('Bebas Neue', 16))
        tvcount.configure(fg='black')
        tvcount.place(relx=0.35, rely=0.8)


    generategraph = tkinter.Button(primewindow, image=primegraphimage, command=primegraph)
    generategraph.configure(bg='white')
    generategraph.place(relx=0.32, rely=0.7)

def Hulu():
    huluwindow = Toplevel(root)
    huluwindow.configure(bg='#1C1C1C')
    huluwindow.title("Hulu")
    huluwindow.geometry("1250x500")

    title = Label(huluwindow, text='Hulu', font=('Bebas Neue', 24))
    title.configure(fg='#3dbb3d', bg='#1C1C1C')
    title.place(relx=0.05, rely=0.05)

    huludescription = '''    Hulu is an American subscription streaming service majority-owned by The 
    Walt Disney Company, with Comcast’s NBCUniversal holding a minority stake. 
    Launched on October 29, 2007, it offers a library of films and TV series 
    from networks such as ABC, Freeform or FX, as well as Hulu originals.'''

    Textwindow = Text(huluwindow, height=7, width=80)

    Textwindow.place(relx=0.075, rely=0.17)
    Textwindow.insert('end', huludescription)
    Textwindow.configure(state='disabled', font=('Bebas Neue',16), fg='white', bg='#1C1C1C', bd=0)

    def huluwiki():
        webbrowser.open("https://en.wikipedia.org/wiki/Hulu")

    learnmore = tkinter.Button(Textwindow, text="Learn More", font =('Bebas Neue', 12), command=huluwiki)
    #learnmore.configure(fg='#E50914',bg='#1C1C1C')
    learnmore.place(relx=0.35, rely=0.65)

    def huluimage():
        webbrowser.open("https://www.hulu.com/welcome")

    logoinfo = tkinter.Button(huluwindow, command=huluimage, image=Hululogo, bd=0, bg='black')
    logoinfo.place(relx=0.7, rely=0.1)


    def hulugraph():
        hulugwindow = Toplevel(huluwindow)
        hulugwindow.configure(bg='white')
        hulugwindow.title("hulu_Graphs")
        hulugwindow.geometry("1500x700")

        hulustats = pd.read_csv(r"C:\Users\potte\Documents\Mini_project_sem-2\Python\datasets\hulu_titles.csv")
        hulustats = hulustats.sort_values(by=["release_year"], ascending=False)

        type = list(hulustats["type"])
        listed_in = list(hulustats["listed_in"])
        country = list(hulustats["country"])
        release_year = list(hulustats["release_year"])

        genre = ['Comedy','Action','Horror','Romance','Family','Drama', 'Docu']

        genremcount = []
        for x in range(1, 8):
            genremcount.append(0)

        for x in listed_in:
            if "Comedy" in str(x):
                genremcount[0] += 1
            if "Action" in str(x):
                genremcount[1] += 1
            if "Horror" in str(x):
                genremcount[2] += 1
            if "Romance" in str(x) or "Entertainment" in str(x):
                genremcount[3] += 1
            if "Kids" in str(x):
                genremcount[4] += 1
            if "Drama" in str(x):
                genremcount[5] += 1
            if "Documentary" in str(x):
                genremcount[6] += 1

        eras = []
        eracount = []
        for x in range(1, 8):
            eracount.append(0)

        for x in range(1960, 2030, 10):
            eras.append(str(x) + "'s")

        for x in release_year:
            if x < 2000:
                if x in range(1960, 1970):
                    eracount[0] += 1
                elif x in range(1970, 1980):
                    eracount[1] += 1
                elif x in range(1980, 1990):
                    eracount[2] += 1
                else:
                    eracount[3] += 1
            else:
                if x in range(2000, 2010):
                    eracount[4] += 1
                elif x in range(2010, 2020):
                    eracount[5] += 1
                else:
                    eracount[6] += 1

        origin = ['Australia', 'U.S.', 'Canada', 'India', 'U.K.', 'Others']
        originmcount = []
        for x in range(1, 7):
            originmcount.append(0)

        for x in country:
            if "Australia" in str(x):
                originmcount[0] += 1
            elif "United States" in str(x):
                originmcount[1] += 1
            elif "Canada" in str(x):
                originmcount[2] += 1
            elif "India" in str(x):
                originmcount[3] += 1
            elif "United Kingdom" in str(x):
                originmcount[4] += 1
            elif "France" in str(x) or "Spain" in str(x) or "Italy" in str(x):
                originmcount[5] += 1

        data1 = {"Genre": genre, "Movie Count": genremcount}
        df1 = pd.DataFrame(data1, columns=['Genre', 'Movie Count'])

        data3 = {"Year": eras, "Movie count": eracount}
        df3 = pd.DataFrame(data3, columns=['Year', 'Movie count'])

        figure1 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, hulugwindow)
        line1.get_tk_widget().grid(row=2, column=1, columnspan=5, rowspan=6)
        df1 = df1[['Genre', 'Movie Count']].groupby('Genre').sum()
        df1.plot(kind='line', ax=ax1, color='#b32222', marker='o', fontsize=10)
        ax1.set_title('Different Genres of movies on hulu')

        figure2 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax2 = figure2.add_subplot(111)
        colors = ['#66b3ff', '#99ff99', '#bf9bde', '#ffcc99', '#ff9999', '#effd5f']
        explode = [0, 0.05, 0, 0, 0, 0]
        ax2.pie(originmcount, autopct=lambda pct: "{:1.1f}%".format(pct), colors=colors,explode=explode, shadow=True)
        ax2.legend(origin)
        pie2 = FigureCanvasTkAgg(figure2, hulugwindow)
        pie2.get_tk_widget().grid(row=2, column=10, columnspan=5, rowspan=6)
        pie2.draw()
        ax2.set_title('Movies on hulu from different countries')

        figure3 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax3 = figure3.add_subplot(111)
        bar3 = FigureCanvasTkAgg(figure3, hulugwindow)
        bar3.get_tk_widget().grid(row=2, column=20, columnspan=5, rowspan=6)
        df3 = df3[['Year', 'Movie count']].groupby('Year').sum()
        df3.plot(kind='bar', color= '#0291bc', legend=True, ax=ax3)
        ax3.set_title('Movies on hulu from different eras')

        hulumoviecount = 0
        hulushowcount = 0

        for x in type:
            if x== "Movie":
                hulumoviecount += 1
            else:
                hulushowcount += 1

        def dispmcount():
            mcount['text'] = "Number of movies in hulu : " + str(hulumoviecount)
            mcount['fg'] = '#3dbb3d'

        def disptvcount():
            tvcount['text'] = "Number of TV shows in hulu : " + str(hulushowcount)
            tvcount['fg'] = '#3dbb3d'

        mcount = tkinter.Button(hulugwindow, text ='Click to display number of movies in hulu', command=dispmcount, font=('Bebas Neue',16))
        mcount.configure(fg='black')
        mcount.place(relx=0.36, rely=0.75)
        tvcount = tkinter.Button(hulugwindow, text='Click to display number of TV shows in hulu', command=disptvcount, font=('Bebas Neue', 16))
        tvcount.configure(fg='black')
        tvcount.place(relx=0.35, rely=0.8)


    generategraph = tkinter.Button(huluwindow, image=hulugraphimage, command=hulugraph)
    generategraph.configure(bg='white')
    generategraph.place(relx=0.32, rely=0.65)

def Hotstar():
    hotstarwindow = Toplevel(root)
    hotstarwindow.configure(bg='#1C1C1C')
    hotstarwindow.title("hotstar")
    hotstarwindow.geometry("1250x500")

    title = Label(hotstarwindow, text='hotstar', font=('Bebas Neue', 24))
    title.configure(fg='#153866', bg='#1C1C1C')
    title.place(relx=0.05, rely=0.05)

    hotstardescription = '''        Disney+ Hotstar (also known as Hotstar) is an Indian brand
     of subscription video on-demand over-the-top streaming service owned by 
     Novi Digital Entertainment of Disney Star and operated by Disney Media 
     and Entertainment Distribution, both divisions of The Walt Disney Company.'''

    Textwindow = Text(hotstarwindow, height=6.5, width=80)

    Textwindow.place(relx=0.075, rely=0.17)
    Textwindow.insert('end', hotstardescription)
    Textwindow.configure(state='disabled', font=('Bebas Neue',16), fg='white', bg='#1C1C1C', bd=0)

    def hotstarwiki():
        webbrowser.open("https://en.wikipedia.org/wiki/hotstar")

    learnmore = tkinter.Button(Textwindow, text="Learn More", font =('Bebas Neue', 12), command=hotstarwiki)
    #learnmore.configure(fg='#E50914',bg='#1C1C1C')
    learnmore.place(relx=0.35, rely=0.65)

    def hotstarimage():
        webbrowser.open("https://www.hotstar.com/in")

    logoinfo = tkinter.Button(hotstarwindow, command=hotstarimage, image=Hotstarlogo, bd=0, bg='black')
    logoinfo.place(relx=0.7, rely=0.1)


    def hotstargraph():
        hotstargwindow = Toplevel(hotstarwindow)
        hotstargwindow.configure(bg='white')
        hotstargwindow.title("hotstar_Graphs")
        hotstargwindow.geometry("1500x700")

        hotstarstats = pd.read_csv(r"C:\Users\potte\Documents\Mini_project_sem-2\Python\datasets\disney_plus_titles.csv")
        hotstarstats = hotstarstats.sort_values(by=["release_year"], ascending=False)

        type = list(hotstarstats["type"])
        listed_in = list(hotstarstats["listed_in"])
        country = list(hotstarstats["country"])
        release_year = list(hotstarstats["release_year"])

        genre = ['Comedy','Action','Horror','Romance','Family','Drama', 'Docu']

        genremcount = []
        for x in range(1, 8):
            genremcount.append(0)

        for x in listed_in:
            if "Comedy" in str(x):
                genremcount[0] += 1
            if "Action" in str(x):
                genremcount[1] += 1
            if "Horror" in str(x):
                genremcount[2] += 1
            if "Romance" in str(x):
                genremcount[3] += 1
            if "Kids" in str(x):
                genremcount[4] += 1
            if "Drama" in str(x):
                genremcount[5] += 1
            if "Documentary" in str(x):
                genremcount[6] += 1

        eras = []
        eracount = []
        for x in range(1, 8):
            eracount.append(0)

        for x in range(1960, 2030, 10):
            eras.append(str(x) + "'s")

        for x in release_year:
            if x < 2000:
                if x in range(1960, 1970):
                    eracount[0] += 1
                elif x in range(1970, 1980):
                    eracount[1] += 1
                elif x in range(1980, 1990):
                    eracount[2] += 1
                else:
                    eracount[3] += 1
            else:
                if x in range(2000, 2010):
                    eracount[4] += 1
                elif x in range(2010, 2020):
                    eracount[5] += 1
                else:
                    eracount[6] += 1

        origin = ['U.S.', 'Canada', 'India', 'U.K.', 'Others']
        originmcount = []
        for x in range(1, 6):
            originmcount.append(0)

        for x in country:
            if "United States" in str(x):
                originmcount[0] += 1
            elif "Canada" in str(x):
                originmcount[1] += 1
            elif "India" in str(x):
                originmcount[2] += 1
            elif "United Kingdom" in str(x):
                originmcount[3] += 1
            else:
                originmcount[4] += 1

        data1 = {"Genre": genre, "Movie Count": genremcount}
        df1 = pd.DataFrame(data1, columns=['Genre', 'Movie Count'])

        data3 = {"Year": eras, "Movie count": eracount}
        df3 = pd.DataFrame(data3, columns=['Year', 'Movie count'])

        figure1 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, hotstargwindow)
        line1.get_tk_widget().grid(row=2, column=1, columnspan=5, rowspan=6)
        df1 = df1[['Genre', 'Movie Count']].groupby('Genre').sum()
        df1.plot(kind='line', ax=ax1, color='#b32222', marker='o', fontsize=10)
        ax1.set_title('Different Genres of movies on hotstar')

        figure2 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax2 = figure2.add_subplot(111)
        colors = ['#99ff99', '#bf9bde', '#ffcc99', '#ff9999', '#effd5f']
        explode = [0.05, 0, 0, 0, 0]
        ax2.pie(originmcount, autopct=lambda pct: "{:1.1f}%".format(pct), colors=colors,explode=explode, shadow=True)
        ax2.legend(origin)
        pie2 = FigureCanvasTkAgg(figure2, hotstargwindow)
        pie2.get_tk_widget().grid(row=2, column=10, columnspan=5, rowspan=6)
        pie2.draw()
        ax2.set_title('Movies on hotstar from different countries')

        figure3 = plt.Figure(figsize=(5, 5), dpi= 92)
        ax3 = figure3.add_subplot(111)
        bar3 = FigureCanvasTkAgg(figure3, hotstargwindow)
        bar3.get_tk_widget().grid(row=2, column=20, columnspan=5, rowspan=6)
        df3 = df3[['Year', 'Movie count']].groupby('Year').sum()
        df3.plot(kind='bar', color= '#0291bc', legend=True, ax=ax3)
        ax3.set_title('Movies on hotstar from different eras')

        hotstarmoviecount = 0
        hotstarshowcount = 0

        for x in type:
            if x== "Movie":
                hotstarmoviecount += 1
            else:
                hotstarshowcount += 1

        def dispmcount():
            mcount['text'] = "Number of movies in hotstar : " + str(hotstarmoviecount)
            mcount['fg'] = '#153866'

        def disptvcount():
            tvcount['text'] = "Number of TV shows in hotstar : " + str(hotstarshowcount)
            tvcount['fg'] = '#153866'

        mcount = tkinter.Button(hotstargwindow, text ='Click to display number of movies in hotstar', command=dispmcount, font=('Bebas Neue',16))
        mcount.configure(fg='black')
        mcount.place(relx=0.36, rely=0.75)
        tvcount = tkinter.Button(hotstargwindow, text='Click to display number of TV shows in hotstar', command=disptvcount, font=('Bebas Neue', 16))
        tvcount.configure(fg='black')
        tvcount.place(relx=0.35, rely=0.8)


    generategraph = tkinter.Button(hotstarwindow, image=hotstargraphimage, command=hotstargraph)
    generategraph.configure(bg='white')
    generategraph.place(relx=0.32, rely=0.6)


def Compare():
    comparewindow = Toplevel(root)
    comparewindow.configure(bg='#1C1C1C')
    comparewindow.title("compare")
    comparewindow.geometry("1250x500")

    title = Label(comparewindow, text='compare', font=('Bebas Neue', 24))
    title.configure(fg='#153866', bg='#1C1C1C')
    title.place(relx=0.05, rely=0.05)

    figure1 = plt.Figure(figsize=(5, 5), dpi=92)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, comparegwindow)
    line1.get_tk_widget().grid(row=2, column=1, columnspan=5, rowspan=6)
    df1 = df1[['Genre', 'Movie Count']].groupby('Genre').sum()
    df1.plot(kind='line', ax=ax1, color='#b32222', marker='o', fontsize=10)
    ax1.set_title('Different Genres of movies on compare')

    figure2 = plt.Figure(figsize=(5, 5), dpi=92)
    ax2 = figure2.add_subplot(111)
    colors = ['#99ff99', '#bf9bde', '#ffcc99', '#ff9999', '#effd5f']
    explode = [0.05, 0, 0, 0, 0]
    ax2.pie(originmcount, autopct=lambda pct: "{:1.1f}%".format(pct), colors=colors, explode=explode, shadow=True)
    ax2.legend(origin)
    pie2 = FigureCanvasTkAgg(figure2, comparegwindow)
    pie2.get_tk_widget().grid(row=2, column=10, columnspan=5, rowspan=6)
    pie2.draw()
    ax2.set_title('Movies on compare from different countries')

    figure3 = plt.Figure(figsize=(5, 5), dpi=92)
    ax3 = figure3.add_subplot(111)
    bar3 = FigureCanvasTkAgg(figure3, comparegwindow)
    bar3.get_tk_widget().grid(row=2, column=20, columnspan=5, rowspan=6)
    df3 = df3[['Year', 'Movie count']].groupby('Year').sum()
    df3.plot(kind='bar', color='#0291bc', legend=True, ax=ax3)
    ax3.set_title('Movies on compare from different eras')

    generategraph = tkinter.Button(comparewindow, image=comparegraphimage, command=comparegraph)
    generategraph.configure(bg='white')
    generategraph.place(relx=0.32, rely=0.6)

netflixbutton = tkinter.Button(root, text='Netflix', command=Netflix, image=Netflixlogo, padx = 5, pady = 5)
netflixbutton.place(relx=0.25, rely=0.2)
primebutton = tkinter.Button(root, text='Prime', command=Prime, image=Primelogo,  padx = 5, pady = 5)
primebutton.place(relx=0.53, rely=0.5)
hulubutton = tkinter.Button(root, text='Hulu', command=Hulu, image=Hululogo,  padx = 5, pady = 5)
hulubutton.place(relx=0.53, rely=0.2)
hotstarbutton = tkinter.Button(root, text='compare', command=Hotstar, image=Hotstarlogo, padx = 5, pady = 5)
hotstarbutton.place(relx=0.25, rely=0.5)

#comparebutton = tkinter.Button(root, image=comparelogo, command=Compare, bg='black', activebackground='black', border=0)
#comparebutton.place(relx=0.4, rely=0.8)
exitroot = tkinter.Button(root, image=exitimage, command=root.destroy, bg='black', border=0)
exitroot.place(relx=0.01, rely=0.01)

root.mainloop()