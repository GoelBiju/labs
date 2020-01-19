import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:poke_app/pokemon.dart';

void main() => runApp(MaterialApp(
  title: "Poke App",
  home: HomePage(),

  debugShowCheckedModeBanner: false,
));


class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  var url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json";
  PokeHub pokeHub;

  @override
  void initState() {
    super.initState();

    pokeHub = new PokeHub();
    fetchData();
  }

  fetchData() async {
    var res = await http.get(url);
    print(res.body);
    pokeHub = pokeHubFromJson(res.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Top - action bar
      appBar: AppBar(
        title: Text("Poke App"),
        backgroundColor: Colors.cyan,
      ),

      // body - content
      body: GridView.count(
        crossAxisCount: 2,
        children: pokeHub.pokemon.map((poke) => Padding(
          padding: const EdgeInsets.all(2.0),
          child: Card(
            child: Column(children: <Widget>[
              Container(
                height: 100.0,
                width: 100.0,
                decoration: BoxDecoration(
                  image: DecorationImage(image: NetworkImage(poke.img))
                ),
              ),

              Text(
                poke.name, 
                style: TextStyle(
                  fontSize: 20.0, 
                  fontWeight: FontWeight.bold
                )
              ),
            ]),
          ),
        )).toList(),
      ),

      // Drawer
      drawer: Drawer(),

      // Action button
      floatingActionButton: FloatingActionButton(
        onPressed: (){},
        backgroundColor: Colors.cyan,
        child: Icon(Icons.refresh),
      ),
    );
  }
}
