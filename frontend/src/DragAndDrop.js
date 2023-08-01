import React from "react";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

function DragAndDrop({ availableTrades, portfolio, onDragEnd }) {
    return (
        <DragDropContext onDragEnd={onDragEnd}>
            <div className="tradesContainer">
                <h2>Available Trades</h2>
                <Droppable droppableId="available">
                    {(provided) => (
                        <ul
                            {...provided.droppableProps}
                            ref={provided.innerRef}
                        >
                            {availableTrades.map((trade, index) => (
                                <Draggable
                                    key={trade.symbol}
                                    draggableId={trade.symbol}
                                    index={index}
                                >
                                    {(provided) => (
                                        <li
                                            {...provided.draggableProps}
                                            {...provided.dragHandleProps}
                                            ref={provided.innerRef}
                                        >
                                            {trade.symbol}
                                        </li>
                                    )}
                                </Draggable>
                            ))}
                            {provided.placeholder}
                        </ul>
                    )}
                </Droppable>
            </div>
            <div className="portfolioContainer">
                <h2>Portfolio</h2>
                <Droppable droppableId="portfolio">
                    {(provided) => (
                        <ul
                            {...provided.droppableProps}
                            ref={provided.innerRef}
                        >
                            {portfolio.map((trade, index) => (
                                <Draggable
                                    key={trade.symbol}
                                    draggableId={trade.symbol}
                                    index={index}
                                >
                                    {(provided) => (
                                        <li
                                            {...provided.draggableProps}
                                            {...provided.dragHandleProps}
                                            ref={provided.innerRef}
                                        >
                                            {trade.symbol}
                                        </li>
                                    )}
                                </Draggable>
                            ))}
                            {provided.placeholder}
                        </ul>
                    )}
                </Droppable>
            </div>
        </DragDropContext>
    );
}

export default DragAndDrop;
