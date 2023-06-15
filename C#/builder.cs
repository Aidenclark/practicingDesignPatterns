/*
In this C# implementation, the classes are defined with appropriate properties, methods, and syntax based on the 
Python code provided. The basic structure and logic of the Builder pattern remain the same. The House class has 
properties representing different parts of the house, and the HouseBuilder and its subclasses define the building 
process for different types of houses. The HouseDirector class orchestrates the construction process. The Main 
method is used for testing and outputting the results.



In the C# code, the get and set keywords are used to define properties in the House class. Properties provide a 
way to encapsulate fields and allow controlled access to their values.

By using properties, you can define the behavior when getting or setting the values of the fields. This allows 
you to add additional logic, such as validation or formatting, before getting or setting the values.

In the House class, the properties Foundation, Walls, Roof, Windows, and Doors are defined using the get and set 
keywords. This allows external code to access and modify these values using the property syntax.
*/






using System;

public class House
{
    public string Foundation { get; set; }
    public string Walls { get; set; }
    public string Roof { get; set; }
    public string Windows { get; set; }
    public string Doors { get; set; }

    public override string ToString()
    {
        return $"Foundation: {Foundation}, Walls: {Walls}, Roof: {Roof}, Windows: {Windows}, Doors: {Doors}";
    }
}

public abstract class HouseBuilder
{
    protected House house;

    public House GetHouse()
    {
        return house;
    }

    public abstract void BuildFoundation();
    public abstract void BuildWalls();
    public abstract void BuildRoof();
    public abstract void BuildWindows();
    public abstract void BuildDoors();
}

public class BasicHouseBuilder : HouseBuilder
{
    public BasicHouseBuilder()
    {
        house = new House();
    }

    public override void BuildFoundation()
    {
        house.Foundation = "Basic foundation";
    }

    public override void BuildWalls()
    {
        house.Walls = "Basic walls";
    }

    public override void BuildRoof()
    {
        house.Roof = "Basic roof";
    }

    public override void BuildWindows()
    {
        house.Windows = "Basic windows";
    }

    public override void BuildDoors()
    {
        house.Doors = "Basic doors";
    }
}

public class FancyHouseBuilder : HouseBuilder
{
    public FancyHouseBuilder()
    {
        house = new House();
    }

    public override void BuildFoundation()
    {
        house.Foundation = "Fancy foundation";
    }

    public override void BuildWalls()
    {
        house.Walls = "Fancy walls";
    }

    public override void BuildRoof()
    {
        house.Roof = "Fancy roof";
    }

    public override void BuildWindows()
    {
        house.Windows = "Fancy windows";
    }

    public override void BuildDoors()
    {
        house.Doors = "Fancy doors";
    }
}

public class HouseDirector
{
    private HouseBuilder builder;

    public HouseDirector(HouseBuilder builder)
    {
        this.builder = builder;
    }

    public void ConstructHouse()
    {
        builder.BuildFoundation();
        builder.BuildWalls();
        builder.BuildRoof();
        builder.BuildWindows();
        builder.BuildDoors();
    }
}

public class Program
{
    public static void Main()
    {
        BasicHouseBuilder basicBuilder = new BasicHouseBuilder();
        FancyHouseBuilder fancyBuilder = new FancyHouseBuilder();

        HouseDirector director = new HouseDirector(basicBuilder);
        director.ConstructHouse();
        House basicHouse = basicBuilder.GetHouse();
        Console.WriteLine("Basic House:");
        Console.WriteLine(basicHouse);

        director = new HouseDirector(fancyBuilder);
        director.ConstructHouse();
        House fancyHouse = fancyBuilder.GetHouse();
        Console.WriteLine("Fancy House:");
        Console.WriteLine(fancyHouse);
    }
}
