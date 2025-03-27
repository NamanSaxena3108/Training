
import java.util.ArrayList;

class Books{
    String title = null;
    String author = null;
    int year = 0;
    String genre = null;
    
    Books(String title, String author, int year) {
        this.title =title;
        this.author = author;
        this.year = year;
    }

    Books(String title, String author, int year,String genre) {
        this.title =title;
        this.author = author;
        this.year = year;
        this.genre = genre;
    }

    public String[] getDetails(){
        return  new String[]{this.title,this.author};
    }

    public static String classDocs(){
        return "This is a book class to take title, author, and year details of each book";
    }

class Library{
    private ArrayList<Books> booklist;

    Library(){
        booklist = new  ArrayList<>();
    }

    public void addBook(Books book){
        booklist.add(book);
    }
}

public class LMS {
    public static  void main(String[] args)
    {
        Books book1 = new Books("Muder on Mile", "Agastha Christien", 1965);   
        Books book2 = new Books("Harry Potter", "J.K.R", 1996);
        Books book3 = new Books("Power of subconsious mind","Josph",1991,"Phscology");

    }
}
