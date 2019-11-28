# CSharp 

- sqlite file db 사용할 때 password setting 관련 
```
using System;
using System.Data.SQLite;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string strConn = @"Data Source=D:\workspace\....\DB.db;Version=3;password=passwordString";

            using (SQLiteConnection conn = new SQLiteConnection(strConn))
            {
                conn.Open();
                conn.ChangePassword("");
                conn.Close();
            }
            Console.WriteLine("Hello World!");
        }
    }
}

```
