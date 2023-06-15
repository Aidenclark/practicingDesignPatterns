






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
